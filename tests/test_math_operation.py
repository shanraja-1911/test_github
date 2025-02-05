import unittest
from src.math_operation import add, subtract

class TestMathOperations(unittest.TestCase):
    """
    Test cases for the math operations module.
    
    This test suite verifies the functionality of basic mathematical operations
    including addition and subtraction with various types of numbers.
    """

    def test_add(self):
        """
        Test the add function with various number combinations.
        
        Test cases include:
        - Positive numbers
        - Negative numbers
        - Floating point numbers
        - Zero as an operand
        """
        # Test positive numbers
        self.assertEqual(add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(add(-1, -1), -2)
        # Test floating point numbers
        self.assertAlmostEqual(add(1.5, 2.7), 4.2)
        # Test zero
        self.assertEqual(add(0, 5), 5)

    def test_subtract(self):
        """
        Test the subtract function with various number combinations.
        
        Test cases include:
        - Positive numbers
        - Negative numbers
        - Floating point numbers
        - Zero as an operand
        """
        # Test positive numbers
        self.assertEqual(subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(subtract(-1, -1), 0)
        # Test floating point numbers
        self.assertAlmostEqual(subtract(5.5, 2.2), 3.3)
        # Test zero
        self.assertEqual(subtract(5, 0), 5)

if __name__ == '__main__':
    unittest.main() 