#!/usr/bin/python3
"""
Unittest for 6-max_integer.py 
function max_integer([...])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests"""

    def test_max_integer_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 4, 6]), 6)

    def test_max_integer_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -4, -6]), -1)

    def test_max_integer_single_number(self):
        self.assertEqual(max_integer([6]), 6)

    def test_max_integer_single_number_zero(self):
        self.assertEqual(max_integer([0]), 0)

    def test_max_integer_floats(self):
        self.assertEqual(max_integer([6.4, -7.8]), 6.4)

    def test_max_integer_num_and_str(self):
        with self.assertRaises(TypeError):
            max_integer([9, '9'])
    
    def test_max_integer_tuple(self):
        with self.assertRaises(TypeError):
            max_integer(3, 5)

    def test_max_integer_tuple_in_list(self):
        with self.assertRaises(TypeError):
            max_integer([4, (3, 5)])
