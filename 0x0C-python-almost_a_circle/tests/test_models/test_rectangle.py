#!/usr/bin/python3
"""
module: test_rectangle.py
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
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

    def test_wrong_amount_attrs(self):
        """raise error with no args pass"""
        with self.assertRaises(TypeError):
            tes = Rectangle()

    def test_wrong_amount_attrs_1(self):
        """ Test error raise with one arg passed"""
        with self.assertRaises(TypeError):
            tes = Rectangle(1)

    def test_access_private_attrs(self):
        """ Test to access to a private attribute """
        tes = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            tes.__width

    def test_access_private_attrs_2(self):
        """ Test to access to a private attribute """
        tes = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            tes.__height

    def test_access_private_attrs_3(self):
        """ Test to access to a private attribute """
        tes = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            tes.__x

    def test_access_private_attrs_4(self):
        """ Test to access to a private attribute """
        tes = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            tes.__y

    def test_attrs_values(self):
        """ test: Trying to pass invalid values """
        with self.assertRaises(ValueError):
            tes = Rectangle(0, 1)

    def test_attrs_values_1(self):
        """ test: Trying to pass invalid values """
        with self.assertRaises(ValueError):
            tes = Rectangle(1, 0)

    def test_attrs_values_2(self):
        """ test: Trying to pass invalid values """
        with self.assertRaises(ValueError):
            tes = Rectangle(1, 1, -3)

    def test_attrs_values_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            tes = Rectangle(2, 1, 1, -1)

    def test_validate_attrs(self):
        """ test: Trying to pass a string value """
        with self.assertRaises(TypeError):
            tes = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs2(self):
        """ test: Trying to pass a string value """
        with self.assertRaises(TypeError):
            tes = Rectangle(2, "2", 2, 2, 2)

    def test_validate_attrs3(self):
        """ test: Trying to pass a string value """
        with self.assertRaises(TypeError):
            tes = Rectangle(2, 2, "2", 2, 2)

    def test_validate_attrs4(self):
        """ test: Trying to pass a string value """
        with self.assertRaises(TypeError):
            tes = Rectangle(2, 2, 2, "2", 2)

    def test_compare_rectangles(self):
        """ compare two  rectangle instance """
        tes = Rectangle(1, 1)
        tes2 = Rectangle(1, 1)
        self.assertEqual(False, tes is tes2)
        self.assertEqual(False, tes.id == tes2.id)

    def test_area1(self):
        """ test: Checking the return value of area method """
        tes = Rectangle(3, 5)
        self.assertEqual(tes.area(), 15)

    def test_area2(self):
        """ test:Checking the return value of area method """
        tes = Rectangle(1, 2)
        self.assertEqual(tes.area(), 2)
        tes.width = 5
        self.assertEqual(tes.area(), 10)
        tes.height = 10
        self.assertEqual(tes.area(), 50)

    def test_area3(self):
        """ test: Checking the return value of area method """
        tes = Rectangle(5, 8)
        self.assertEqual(tes.area(), 40)
        tes2 = Rectangle(10, 5)
        self.assertEqual(tes2.area(), 50)

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 8)

    def test_check_value2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -7)

    def test_create(self):
        """ Test the create method """
        dictionary = {'id': 88}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 88)

    def test_create2(self):
        """ Test the create method """
        dictionary = {'id': 88, 'width': 61}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 88)
        self.assertEqual(r1.width, 61)

    def test_create3(self):
        """ Test the create method """
        dictionary = {'id': 88, 'width': 61, 'height': 20}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 88)
        self.assertEqual(r1.width, 61)
        self.assertEqual(r1.height, 20)

    def test_create4(self):
        """ Test the create method """
        dictionary = {'id': 88, 'width': 61, 'height': 52, 'x': 30}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 88)
        self.assertEqual(r1.width, 61)
        self.assertEqual(r1.height, 52)
        self.assertEqual(r1.x, 30)

    def test_create5(self):
        """ Test the create method """
        dictionary = {'id': 88, 'width': 61, 'height': 52, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 88)
        self.assertEqual(r1.width, 61)
        self.assertEqual(r1.height, 52)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        linput = [r1, r2]
        Rectangle.save_to_file(linput)
        loutput = Rectangle.load_from_file()

        for i in range(len(linput)):
            self.assertEqual(linput[i].__str__(), loutput[i].__str__())
