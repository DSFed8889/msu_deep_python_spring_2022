import unittest
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

    def test_class_attrs(self):
        self.assertEqual(CustomClass.custom_x, 50)
        CustomClass.custom_line
        CustomClass.__init__
        with self.assertRaises(Exception):
            CustomClass.new_attr
            CustomClass.custom_new_attr
        CustomClass.new_attr = 0
        self.assertEqual(CustomClass.custom_new_attr, 0)
        CustomClass.new_attr = 5
        self.assertEqual(CustomClass.custom_new_attr, 5)
        CustomClass.custom_new_attr = 0
        self.assertEqual(CustomClass.custom_new_attr, 0)
        CustomClass.custom_new_attr

        CustomClass.__attr = 'string'
        with self.assertRaises(Exception):
            CustomClass.__attr
        self.assertEqual(CustomClass.custom__TestMetaClass__attr, 'string')

        self.assertEqual(CustomClass.custom_line(self.ob), 100)

    def test_ob_attrs(self):
        self.assertEqual(self.ob.custom_x, 50)
        self.assertEqual(self.ob.custom_val, 99)
        self.ob.custom_line
        self.assertEqual(self.ob.custom_line(), 100)
        self.ob.__init__
        with self.assertRaises(Exception):
            self.ob.new_attr
            self.ob.custom_new_attr
        self.ob.new_attr = 0
        self.assertEqual(self.ob.custom_new_attr, 0)
        self.ob.new_attr = 5
        self.assertEqual(self.ob.custom_new_attr, 5)
        self.ob.custom_new_attr = 0
        self.assertEqual(self.ob.custom_new_attr, 0)
        self.ob.custom_new_attr

        self.ob._attr = {'string': 120}
        with self.assertRaises(Exception):
            self.ob.__attr
        self.assertEqual(self.ob.custom__attr, {'string': 120})

        self.ob.__attr = 'string'
        with self.assertRaises(Exception):
            self.ob.__attr
        self.assertEqual(self.ob.custom__TestMetaClass__attr, 'string')

        self.assertEqual(self.ob.custom_line(), 100)
        self.assertEqual(str(self.ob), 'Custom_by_metaclass')
