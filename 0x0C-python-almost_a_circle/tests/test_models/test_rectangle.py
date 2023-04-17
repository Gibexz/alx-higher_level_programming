#!/usr/bin/pyhton3
"""
module: test_rectangle.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """
    unittest for module for rectangle class
    """
    def setUp(self):
        """Runs before each test"""
        Base._Base__nb_objects = 0

    def test_rectangle1(self):
        """Rectangle with 4 args and no id specified"""
        tes = Rectangle(1, 2, 3, 4)
        self.assertEqual(tes.width, 1)
        self.assertEqual(tes.height, 2)
        self.assertEqual(tes.x, 3)
        self.assertEqual(tes.y, 4)
        self.assertEqual(tes.id, 1)

    def test_rectangle2(self):
        """Rectangle with 4 args and id specified"""
        tes = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(tes.width, 1)
        self.assertEqual(tes.height, 2)
        self.assertEqual(tes.x, 3)
        self.assertEqual(tes.y, 4)
        self.assertEqual(tes.id, 5)

    def test_rectangle3(self):
        """Rectangle with on;y 2 args"""
        tes = Rectangle(1, 2)
        self.assertEqual(tes.width, 1)
        self.assertEqual(tes.height, 2)
        self.assertEqual(tes.x, 0)
        self.assertEqual(tes.y, 0)
        self.assertEqual(tes.id, 1)

    def test_base_instance(self):
        """checks if Rectangle is an of Base"""
        tes = Rectangle(1, 2)
        self.assertEqual(True, isinstance(tes, Base))
