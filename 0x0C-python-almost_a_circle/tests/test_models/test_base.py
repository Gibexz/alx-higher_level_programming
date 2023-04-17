#!/usr/bin/python3
"""
module: test_base.py
Unittest of base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Unittest cases for Base class """

    def setUp(self):
        """ Invoked for each test """
        Base._Base__nb_objects = 0

    def test_id_None(self):
        """ default test instance where id -= None """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_NotNone(self):
        """ test: instance with an arg """
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_id_NoneS(self):
        """ tests: instances with no arg """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_NotNones(self):
        """ tests: instances with arg """
        b1 = Base(32)
        b2 = Base(23)
        b3 = Base(4)
        self.assertEqual(b1.id, 32)
        self.assertEqual(b2.id, 23)
        self.assertEqual(b3.id, 4)

    def test_id_mixed(self):
        """ tests: mixed, instance with and without arg """
        b1 = Base(20)
        b2 = Base()
        b3 = Base(3)
        b4 = Base()
        self.assertEqual(b1.id, 20)
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 2)

    def test_with_string(self):
        """tests: arg is a string """
        b1 = Base("99")
        self.assertEqual(b1.id, '99')

    def test_with_multiple_args(self):
        """ tests: with more than one arg """
        with self.assertRaises(TypeError):
            b1 = Base(8, 9)
