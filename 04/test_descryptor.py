import unittest
from contextlib import contextmanager
from descryptor import Data


class TestDescryptor(unittest.TestCase):
    def setUp(self):
        self.data = Data()
        print('Set up')

    def tearDown(self):
        print('Tear down')

    @contextmanager
    def assertNotRaises(self):
        try:
            yield None
        except Exception:
            raise AssertionError('{} raised'.format(Exception.__name__))

    def assign_num(self, value):
        self.data.num = value

    def assign_name(self, value):
        self.data.name = value

    def assign_price(self, value):
        self.data.price = value

    def test_assign_num(self):
        with self.assertNotRaises():
            self.assign_num(0)
        self.assertEqual(self.data.num, 0)
        with self.assertNotRaises():
            self.assign_num(1)
        self.assertEqual(self.data.num, 1)
        with self.assertNotRaises():
            self.assign_num(2)
        self.assertEqual(self.data.num, 2)
        with self.assertNotRaises():
            self.assign_num(-10000)
        self.assertEqual(self.data.num, -10000)
        with self.assertNotRaises():
            self.assign_num(500)
        self.assertEqual(self.data.num, 500)
        with self.assertNotRaises():
            self.assign_num(11111111111111)
        self.assertEqual(self.data.num, 11111111111111)
        with self.assertNotRaises():
            self.assign_num(-1)
        self.assertEqual(self.data.num, -1)
        with self.assertNotRaises():
            self.assign_num(-2)
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(ValueError):
            self.assign_num('string')
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(ValueError):
            self.assign_num([])
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(ValueError):
            self.assign_num([0])
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(ValueError):
            self.assign_num([2, 2])
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(ValueError):
            self.assign_num(['str'])
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(ValueError):
            self.assign_num({})
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(ValueError):
            self.assign_num({'string': 'str'})
        self.assertEqual(self.data.num, -2)

    def test_assign_name(self):
        with self.assertNotRaises():
            self.assign_name('')
        self.assertEqual(self.data.name, '')
        with self.assertNotRaises():
            self.assign_name('asdf')
        self.assertEqual(self.data.name, 'asdf')
        with self.assertNotRaises():
            self.assign_name('12')
        self.assertEqual(self.data.name, '12')
        with self.assertNotRaises():
            self.assign_name('df sdf sdf')
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name(0)
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name(1)
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name(-1)
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name([])
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name([0])
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name([2, 2])
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name(['str'])
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name({})
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(ValueError):
            self.assign_name({'string': 'str'})
        self.assertEqual(self.data.name, 'df sdf sdf')

    def test_assign_price(self):
        with self.assertNotRaises():
            self.assign_price(1)
        self.assertEqual(self.data.price, 1)
        with self.assertNotRaises():
            self.assign_price(2)
        self.assertEqual(self.data.price, 2)
        with self.assertNotRaises():
            self.assign_price(10000)
        self.assertEqual(self.data.price, 10000)
        with self.assertNotRaises():
            self.assign_price(500)
        self.assertEqual(self.data.price, 500)
        with self.assertNotRaises():
            self.assign_price(11111111111111)
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price(0)
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price(-1)
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price(-123123123)
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price('string')
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price([])
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price([0])
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price([2, 2])
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price(['str'])
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price({})
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(ValueError):
            self.assign_price({'string': 'str'})
        self.assertEqual(self.data.price, 11111111111111)
