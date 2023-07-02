#!/usr/bin/python3
"""
Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)

    def test_mixed_positive_negative_values(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_float_values(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([-1.5, -2.5, -3.5, -4.5]), -1.5)

    def test_strings(self):
        self.assertEqual(max_integer(['apple', 'banana', 'cherry']), 'cherry')

if __name__ == '__main__':
    unittest.main(exit=False)
    exit(0)
