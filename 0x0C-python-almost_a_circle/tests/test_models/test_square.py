#!/usr/bin/python3
"""
module: test_square.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """ unittest for square class"""
    def setUp(self):
        """runs befor each test case"""
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Test new square """
        tes = Square(5)
        self.assertEqual(tes.size, 5)
        self.assertEqual(tes.width, 5)
        self.assertEqual(tes.height, 5)
        self.assertEqual(tes.x, 0)
        self.assertEqual(tes.y, 0)
        self.assertEqual(tes.id, 1)

    def test_new_square2(self):
        """ Test new square with complete attrs """
        new = Square(2, 5, 5, 4)
        self.assertEqual(new.size, 2)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_squares(self):
        """ compare new squares """
        new = Square(1, 1)
        new2 = Square(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_if_Base_instance(self):
        """ Test if the Square is a Base instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Base))

    def test_if_Rectangle_instance(self):
        """ Test if the Square is a Rectangle instance """
        new = Square(1)
        self.assertEqual(True, isinstance(new, Rectangle))

    def test_wrong_amount_attrs(self):
        """ Test: error raise with no args passed """
        with self.assertRaises(TypeError):
            new = Square()

    def test_wrong_amount_attrs1(self):
        """ Test: error raised with more args passed """
        with self.assertRaises(TypeError):
            new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        """ test: accessing private attribute """
        new = Square(4)
        with self.assertRaises(AttributeError):
            new.__width

    def test_access_private_attrs2(self):
        """ test: accessing private attribute """
        new = Square(1)
        with self.assertRaises(AttributeError):
            new.__height

    def test_access_private_attrs3(self):
        """ test: accessing private attribute """
        new = Square(2)
        with self.assertRaises(AttributeError):
            new.__y

    def test_access_private_attrs4(self):
        """ test: accessing private attribute """
        new = Square(3)
        with self.assertRaises(AttributeError):
            new.__x

    def test_validate_attrs1(self):
        """ test: Trying to pass a string value """
        with self.assertRaises(TypeError):
            ted = Square("2", 7, 2, 2)

    def test_validate_attrs2(self):
        """ test: Trying to pass a string value """
        with self.assertRaises(TypeError):
            tes = Square(2, "7", 2, 2)

    def test_validate_attrs3(self):
        """ test: passing a string value """
        with self.assertRaises(TypeError):
            tes = Square(2, 7, "2", 2)

    def test_value_attrs1(self):
        """ test: passing invalid values """
        with self.assertRaises(ValueError):
            tes = Square(0)

    def test_value_attrs2(self):
        """ test: passing invalid values """
        with self.assertRaises(ValueError):
            ted = Square(1, -7)

    def test_value_attrs_3(self):
        """ test: passing invalid values """
        with self.assertRaises(ValueError):
            new = Square(1, 1, -7)

    def test_area(self):
        """ Checking the return value of area method """
        new = Square(8)
        self.assertEqual(new.area(), 64)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Square.load_from_file()
        self.assertEqual(load_file, load_file)

    def test_area2(self):
        """ Checking the return value of area method """
        new = Square(2)
        self.assertEqual(new.area(), 4)
        new.size = 5
        self.assertEqual(new.area(), 25)

    def test_value_square(self):
        """ Test value pased to Square """
        with self.assertRaises(ValueError):
            s1 = Square(-1)

    def test_create1(self):
        """ Test create method """
        dictionary = {'id': 88}
        s1 = Square.create(**dictionary)
        self.assertEqual(s1.id, 88)

    def test_create2(self):
        """ Test create method """
        dictionary = {'id': 88, 'size': 10}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 88)
        self.assertEqual(s1.size, 10)

    def test_create3(self):
        """ Test create method """
        dictionary = {'id': 88, 'size': 10, 'x': 2}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 88)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)

    def test_create4(self):
        """ Test create method """
        dictionary = {'id': 88, 'size': 10, 'x': 2, 'y': 3}
        s1 = Rectangle.create(**dictionary)
        self.assertEqual(s1.id, 88)
        self.assertEqual(s1.size, 10)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)

    def test_load_from_file_2(self):
        """ Test load JSON file """
        s1 = Square(5)
        s2 = Square(8, 2, 5)

        linput = [s1, s2]
        Square.save_to_file(linput)
        loutput = Square.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
