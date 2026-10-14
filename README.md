Stack-Based Mathematical Expression Evaluator

 1. Project Information

Project Title: Stack Implementation for Mathematical Expression Evaluation

Course Code: DCOMP320

Course Title: Data Structures and Algorithm

Programming Language: Python

Student Name: [Petros Joel Kamara]

Lecturer: Miss Hawa Kallon

Semester: 5

---

 2. Project Description

This project implements a mathematical expression evaluator using
the stack data structure in Python.

The program reads mathematical expressions from an input file
named `input.txt`, evaluates the expressions using two stacks,
and writes the calculated results to an output file named
`output.txt`.

The program supports addition, subtraction, multiplication,
division, parentheses, and decimal numbers.

It follows standard mathematical operator precedence and
includes error handling for invalid expressions and division
by zero.

---

 3. Project Objectives

The objectives of this project are:

- To implement a Stack class in Python.
- To demonstrate the Last-In, First-Out (LIFO) principle.
- To evaluate mathematical expressions using two stacks.
- To apply mathematical operator precedence correctly.
- To process expressions from a text file.
- To write calculated results to an output file.
- To detect invalid expressions and division-by-zero errors.
- To demonstrate the practical application of data structures
  and algorithms.

---

 4. Project Files

The project contains the following files:

 main.py

Contains the Python source code responsible for reading,
evaluating, and processing mathematical expressions.

 input.txt

Contains the mathematical expressions that the program
will evaluate.

 output.txt

Stores the results produced by the program after execution.

 README.md

Provides information about the project, its requirements,
supported operations, and instructions for running it.

---

 5. Technologies Used

- Python 3
- Visual Studio Code
- Regular expressions
- Stack data structure
- Text-file processing

No third-party Python packages are required.

---

 6. System Requirements

The program requires:

- A computer running Windows, macOS, or Linux.
- Python 3 installed on the computer.
- Visual Studio Code or another Python editor.
- The project files stored in the same directory.

---

 7. How to Run the Program

Follow these steps to execute the program.

1. Install Python 3 on your computer.
2. Open the project folder in Visual Studio Code.
3. Ensure that `main.py` and `input.txt` are in the same folder.
4. Open the integrated terminal in Visual Studio Code.
5. Run the following command:

   `python main.py`

6. If your computer uses the `python3` command, run:

   `python3 main.py`

7. Wait for the program to finish processing the expressions.
8. Open `output.txt` to view the calculated results.

The program generates or updates `output.txt` automatically.

---

 8. Supported Mathematical Operations

The program supports the following operators:

| Operator | Operation |
|----------|-----------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| ( ) | Parentheses |

Decimal numbers are also supported.

---

 9. Operator Precedence

The program follows standard mathematical precedence.

1. Parentheses are evaluated first.
2. Multiplication and division have higher precedence than
   addition and subtraction.
3. Operators with equal precedence are processed from
   left to right.

For example:

`3 + 5 * 2`

Multiplication is performed first:

`5 * 2 = 10`

Then addition is performed:

`3 + 10 = 13`

Therefore, the answer is `13`.

---

 10. Sample Input

The following expressions can be placed in `input.txt`:

    3 + 5 * 2
    -----
    (8 / 4) + 7 * 2
    -----
    10 - (2 + 3) * 4

---

 11. Expected Output

The expected output for the sample expressions is:

    13
    -----
    16
    -----
    -10

Note: The second expression evaluates to 16 under standard
mathematical precedence.

---

 12. Error Handling

The program detects several common errors, including:

- Invalid characters.
- Missing operands.
- Incomplete mathematical expressions.
- Unmatched parentheses.
- Division by zero.

When an error is encountered, the program writes an explanatory
error message to the output file and continues processing
subsequent lines.

---

 13. Algorithm Complexity

Let n represent the number of tokens in a mathematical expression.

The algorithm processes each token a limited number of times.

**Time Complexity:** O(n)

**Auxiliary Space Complexity:** O(n)

These complexities indicate that the time and memory required
generally increase in proportion to the size of the expression.

---

 14. Limitations

The current implementation does not support:

- Exponentiation.
- Mathematical variables.
- Implicit multiplication, such as `2(3 + 4)`.
- Advanced mathematical functions.

The program is designed for expressions using the supported
arithmetic operators and parentheses.

---

 15. Conclusion

This project demonstrates how stacks can be used to evaluate
mathematical expressions in Python.

The program applies stack operations, operator precedence,
and file processing to calculate mathematical results.

It also demonstrates the importance of input validation,
error handling, testing, and algorithm complexity analysis.

The project provides practical experience in implementing
data structures and applying algorithms to solve a
computational problem.