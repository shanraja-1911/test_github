"""
Basic mathematical operations module.

This module provides simple arithmetic functions for basic mathematical operations
like addition and subtraction. All functions support both integer and floating-point
numbers as inputs.
"""

def add(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a (float): First number to add
        b (float): Second number to add
        
    Returns:
        float: The sum of a and b
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(1.5, 2.5)
        4.0
    """
    return a + b

def subtract(a: float, b: float) -> float:
    """
    Subtract second number from first number.
    
    Args:
        a (float): Number to subtract from (minuend)
        b (float): Number to subtract (subtrahend)
        
    Returns:
        float: The difference between a and b (a - b)
        
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(1, 1)
        0
        >>> subtract(5.5, 2.2)
        3.3
    """
    return a - b
