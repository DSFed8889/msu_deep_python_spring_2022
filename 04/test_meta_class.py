import unittest
from contextlib import contextmanager
from meta_class import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class TestMetaClass(unittest.TestCase):

    def setUp(self):
        self.ob = CustomClass()
        print('Set up')

    def tearDown(self):
        print('Tear down')

    @contextmanager
    def assertNotRaises(self):
        try:
            yield None
        except Exception:
            raise AssertionError(f'{Exception.__name__} raised')

    def test_class_attrs(self):
        with self.assertNotRaises():
            self.assertEqual(CustomClass.custom_x, 50)
            CustomClass.custom_line
            CustomClass.__init__
        with self.assertRaises(Exception):
            CustomClass.new_attr
            CustomClass.custom_new_attr
        with self.assertNotRaises():
            CustomClass.new_attr = 0
            self.assertEqual(CustomClass.custom_new_attr, 0)
            CustomClass.new_attr = 5
            self.assertEqual(CustomClass.custom_new_attr, 5)
            CustomClass.custom_new_attr = 0
            self.assertEqual(CustomClass.custom_new_attr, 0)
            CustomClass.custom_new_attr

    def test_ob_attrs(self):
        with self.assertNotRaises():
            self.assertEqual(self.ob.custom_x, 50)
            self.assertEqual(self.ob.custom_val, 99)
            self.ob.custom_line
            self.ob.__init__
        with self.assertRaises(Exception):
            self.ob.new_attr
            self.ob.custom_new_attr
        with self.assertNotRaises():
            self.ob.new_attr = 0
            self.assertEqual(self.ob.custom_new_attr, 0)
            self.ob.new_attr = 5
            self.assertEqual(self.ob.custom_new_attr, 5)
            self.ob.custom_new_attr = 0
            self.assertEqual(self.ob.custom_new_attr, 0)
            self.ob.custom_new_attr
