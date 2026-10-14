import re
from pathlib import Path


# File paths
BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "input.txt"
OUTPUT_FILE = BASE_DIR / "output.txt"


# ==========================================
# STACK CLASS
# ==========================================

class Stack:
    """Implement a stack using Python lists."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item."""
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise ValueError("Cannot peek at an empty stack.")
        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)


# ==========================================
# TOKENIZATION
# ==========================================

def tokenize(expression):
    """Separate an expression into numbers and operators."""

    pattern = re.compile(r"\d+(?:\.\d+)?|[()+\-*/]")
    tokens = []
    position = 0

    while position < len(expression):

        if expression[position].isspace():
            position += 1
            continue

        match = pattern.match(expression, position)

        if not match:
            raise ValueError(
                f"Invalid character near: {expression[position:]}"
            )

        tokens.append(match.group())
        position = match.end()

    if not tokens:
        raise ValueError("Expression is empty.")

    return tokens


# ==========================================
# OPERATOR PRECEDENCE
# ==========================================

def precedence(operator):
    """Return the precedence of an arithmetic operator."""

    if operator in ("+", "-"):
        return 1

    if operator in ("*", "/"):
        return 2

    return 0


# ==========================================
# APPLY AN OPERATOR
# ==========================================

def apply_operator(numbers, operators):
    """Evaluate the top operator using the top two numbers."""

    operator = operators.pop()

    if numbers.size() < 2:
        raise ValueError("Missing operand.")

    right = numbers.pop()
    left = numbers.pop()

    if operator == "+":
        result = left + right

    elif operator == "-":
        result = left - right

    elif operator == "*":
        result = left * right

    elif operator == "/":
        if right == 0:
            raise ValueError("Division by zero is not allowed.")
        result = left / right

    else:
        raise ValueError(f"Unsupported operator: {operator}")

    numbers.push(result)


# ==========================================
# EXPRESSION EVALUATION
# ==========================================

def evaluate(expression):
    """Evaluate an arithmetic expression using two stacks."""

    tokens = tokenize(expression)

    numbers = Stack()
    operators = Stack()

    expecting_operand = True

    for token in tokens:

        # Numbers
        if re.fullmatch(r"\d+(?:\.\d+)?", token):

            if not expecting_operand:
                raise ValueError(
                    "Missing operator between numbers."
                )

            if "." in token:
                numbers.push(float(token))
            else:
                numbers.push(int(token))

            expecting_operand = False

        # Opening parentheses
        elif token == "(":

            if not expecting_operand:
                raise ValueError(
                    "Missing operator before opening parenthesis."
                )

            operators.push(token)

        # Closing parentheses
        elif token == ")":

            if expecting_operand:
                raise ValueError(
                    "Empty or incomplete parentheses."
                )

            while (
                not operators.is_empty()
                and operators.peek() != "("
            ):
                apply_operator(numbers, operators)

            if operators.is_empty():
                raise ValueError(
                    "Unmatched closing parenthesis."
                )

            operators.pop()
            expecting_operand = False

        # Arithmetic operators
        elif token in ("+", "-", "*", "/"):

            if expecting_operand:

                # Support unary positive and negative signs.
                if token in ("+", "-"):
                    numbers.push(0)
                else:
                    raise ValueError("Unexpected operator.")

            while (
                not operators.is_empty()
                and operators.peek() != "("
                and precedence(operators.peek())
                >= precedence(token)
            ):
                apply_operator(numbers, operators)

            operators.push(token)
            expecting_operand = True

    if expecting_operand:
        raise ValueError("Expression ends with an operator.")

    # Apply remaining operators.
    while not operators.is_empty():

        if operators.peek() == "(":
            raise ValueError("Unmatched opening parenthesis.")

        apply_operator(numbers, operators)

    if numbers.size() != 1:
        raise ValueError("Malformed mathematical expression.")

    return numbers.pop()


# ==========================================
# RESULT FORMATTING
# ==========================================

def format_result(value):
    """Remove unnecessary decimal places from whole numbers."""

    if isinstance(value, float) and value.is_integer():
        return str(int(value))

    return str(value)


# ==========================================
# INPUT FILE PROCESSING
# ==========================================

def is_separator(line):
    """Identify separator lines containing at least three hyphens."""

    return re.fullmatch(r"\s*-{3,}\s*", line) is not None


def process_file():
    """Read expressions and save their results."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "input.txt was not found in the project directory."
        )

    input_lines = INPUT_FILE.read_text(
        encoding="utf-8"
    ).splitlines()

    output_lines = []

    for line_number, line in enumerate(input_lines, start=1):

        if not line.strip():
            output_lines.append(line)
            continue

        if is_separator(line):
            output_lines.append(line)
            continue

        try:
            result = evaluate(line)
            output_lines.append(format_result(result))

        except (ValueError, ZeroDivisionError) as error:
            output_lines.append(
                f"ERROR on line {line_number}: {error}"
            )

    OUTPUT_FILE.write_text(
        "\n".join(output_lines) + "\n",
        encoding="utf-8"
    )

    print("Expression evaluation completed.")
    print(f"Results saved to: {OUTPUT_FILE}")


# ==========================================
# MAIN PROGRAM
# ==========================================

if __name__ == "__main__":
    process_file()