Python Overview (Basics up to Sets)

1. Introduction to Python

Python is a versatile, object-oriented programming language.

It features dynamic typing, eliminating the need for explicit data type declarations.

Known for its clear syntax, making it beginner-friendly.

Extensively used in Data Science, AI, Machine Learning, Web Development, and Automation.

2. Python Libraries

Python provides a rich ecosystem of libraries tailored for various domains:

Data Analysis: NumPy, Pandas

Statistical Computing: SciPy, Statsmodels

Machine Learning: Scikit-learn

Deep Learning: TensorFlow, PyTorch, Keras

Agentic AI: LangChain, AutoGen

Large Language Models: HuggingFace Transformers

Natural Language Processing: NLTK, spaCy

Generative AI: OpenAI, LangChain

Computer Vision: OpenCV

3. Variables

Variables hold data values.

Names can include letters, digits, and underscores but cannot start with a digit.

Case-sensitive and cannot be Python reserved keywords.

Example: user_name, _totalCount

4. Data Types

Defines the nature of data stored in variables:

Integer (int): Whole numbers without decimals (e.g., 10, 42)

Float (float): Numbers with decimal points (e.g., 3.14, 2.0)

Boolean (bool): Represents True or False

Complex (complex): Numbers with real and imaginary parts (e.g., 1+2j)

String (str): Text enclosed in single (' '), double (" "), or triple (''' ''' ) quotes

5. Functions

Functions are reusable blocks of code.

Invoked using parentheses ().

Access functions from objects or modules using dot notation ..

Types:

Built-in: print(), len(), type(), id()

User-defined: Created with def keyword

6. Operators

Operators perform operations on data:

Arithmetic: +, -, *, /, %, **

Assignment: =, +=, -=, *=, /=

Comparison: >, <, ==, !=, >=, <=

Logical: and, or, not

Unary: +x, -x

7. Identifiers

Names assigned to variables, functions, classes, etc.

Must not start with a digit.

Can include letters, digits, and underscores.

Cannot be Python keywords.

8. Statements

Instructions executed by Python.

Example:

x = 10
print(x)

9. Modules and Packages

Module: A Python file containing code (functions, classes).

Package: A directory containing multiple modules.

10. Indexing and Slicing

Python uses zero-based indexing.

Applicable to sequences like lists, tuples, strings, and pandas data structures.

Indexing

Access a single element by its position.

Slicing

Extract a subset of elements.

Syntax:

[:] — all elements

[x:y] — elements from index x to y-1

[:x] — elements from start to x-1

[x:] — elements from x to the end

Step Slicing

Skip elements using a step value.

Syntax: [start:stop:step]

11. Data Structures

Store collections of data.

Two main types:

Structured (Labeled/Supervised): Used in Machine Learning

Unstructured (Unlabeled/Unsupervised): Used in Generative AI and Agentic AI

12. Differences: Data Type vs Data Structure vs Array vs Tensor

Data Type: Holds a single value.

Data Structure: Holds multiple values.

Array: Collection of numbers (1D, 2D, 3D).

Tensor: Multi-dimensional arrays used in Deep Learning.

13. Parameter Tuning

Parameter tuning: System assigns default values.

Hyperparameter tuning: User manually adjusts values.

14. Common Data Structures

List

Tuple

Set

Dictionary

Range

15. List

Defined with square brackets [ ].

Dynamic size (can grow).

Allows duplicates.

Mutable (modifiable).

Can hold multiple data types.

List Methods

append() — add an element

count() — count occurrences

copy() — create a copy

clear() — remove all elements

extend() — add multiple elements

index() — find index of an element

insert() — add element at specific position

pop() — remove element by index

remove() — remove element by value

sort() — sort elements

16. Tuple

Defined with parentheses ( ).

Immutable (cannot be changed).

Supports indexing and slicing.

Allows duplicates.

Tuple Methods:

count()

index()

17. Set

Defined with curly braces { }.

Unordered collection.

No duplicates allowed.

Does not support indexing or slicing.

Supports methods like copy(), remove(), pop().

pop() removes a random element.

Note: Sets may appear ordered but are not sorted.

Set Operations

Union (|): Combines all elements from both sets.

Intersection (&): Elements common to both sets.

Difference (-): Elements in one set but not the other.

Symmetric Difference (^): Elements in either set but not both.

Summary

This page provides a comprehensive overview of Python basics, including variables, data types, functions, operators, identifiers, statements, modules, indexing, data structures, and set operations, forming a solid foundation for further study.
