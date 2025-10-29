# app/operations.py

"""
Module: operations.py

This module contains basic arithmetic functions that perform addition, subtraction,
multiplication, and division of two numbers. These functions are foundational for
building more complex applications, such as calculators or financial tools.

Functions:
- add(a: Union[int, float], b: Union[int, float], c: Union[int, float]) -> Union[int, float]: Returns the sum of a, b, and c.
- subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the difference when b is subtracted from a.
- multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the product of a and b.
- divide(a: Union[int, float], b: Union[int, float]) -> float: Returns the quotient when a is divided by b. Raises ValueError if b is zero.

Usage:
These functions can be imported and used in other modules or integrated into APIs
to perform arithmetic operations based on user input.
"""

from typing import Union  # Import Union for type hinting multiple possible types

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]

def add(a: Number, b: Number, c: Number = 0) -> Number:
    """
    Add three numbers and return the result.
    If c is not provided, it defaults to 0 (no change to the result).

    Parameters:
    - a (int or float): The first number to add.
    - b (int or float): The second number to add.
    - c (int or float, optional): The third number to add. Defaults to 0.

    Returns:
    - int or float: The sum of a, b, and c.

    Example:
    >>> add(2, 3, 4)
    9
    >>> add(2.5, 3, 4)
    9.5
    >>> add(2.5, 3, 6)
    11.5
    >>> add(2, 3)  # c defaults to 0
    5
    """
    # Perform addition of a, b, and c
    result = a + b + c
    return result

def subtract(a: Number, b: Number, c: Number = 0) -> Number:
    """
    Subtract the second and third numbers from the first and return the result.
    If c is not provided, it defaults to 0 (no change to the result).

    Parameters:
    - a (int or float): The number from which to subtract.
    - b (int or float): The number to subtract.
    - c (int or float, optional): The second number to subtract. Defaults to 0.

    Returns:
    - int or float: The difference between a and b and c.

    Example:
    >>> subtract(5, 3, 1)
    1
    >>> subtract(5.5, 2, 0.5)
    3.0
    >>> subtract(5, 3)  # c defaults to 0
    2
    """
    # Perform subtraction of b and c from a
    result = a - b - c
    return result

def multiply(a: Number, b: Number, c: Number = 1) -> Number:
    """
    Multiply three numbers and return the product.
    If c is not provided, it defaults to 1 (no change to the result).

    Parameters:
    - a (int or float): The first number to multiply.
    - b (int or float): The second number to multiply.
    - c (int or float, optional): The third number to multiply. Defaults to 1.

    Returns:
    - int or float: The product of a, b, and c.

    Example:
    >>> multiply(2, 3, 4)
    24
    >>> multiply(2.5, 4, 10)
    100.0
    >>> multiply(2, 3)  # c defaults to 1
    6
    """
    # Perform multiplication of a, b, and c
    result = a * b * c
    return result

def divide(a: Number, b: Number,) -> float:
    """
    Divide the first number by the second and return the quotient.

    Parameters:
    - a (int or float): The dividend.
    - b (int or float): The divisor.

    Returns:
    - float: The quotient of a divided by b.

    Raises:
    - ValueError: If b is zero, as division by zero is undefined.

    Example:
    >>> divide(6, 3)
    2.0
    >>> divide(5.5, 2)
    2.75
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero!
    """
    # Check if the divisor is zero to prevent division by zero
    if b == 0:
        # Raise a ValueError with a descriptive message
        raise ValueError("Cannot divide by zero!")
    
    # Perform division of a by b and return the result as a float
    result = a / b
    return result
