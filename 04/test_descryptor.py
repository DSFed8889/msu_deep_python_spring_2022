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
            raise AssertionError(f'{Exception.__name__} raised')

    def test_assign_num(self):
        with self.assertNotRaises():
            self.data.num = 0
            self.data.num
            self.assertEqual(self.data.num, 0)
            self.data.num = 1
            self.data.num
            self.assertEqual(self.data.num, 1)
            self.data.num = 2
            self.data.num
            self.assertEqual(self.data.num, 2)
            self.data.num = -10000
            self.data.num
            self.assertEqual(self.data.num, -10000)
            self.data.num = 500
            self.data.num
            self.assertEqual(self.data.num, 500)
            self.data.num = 11111111111111
            self.data.num
            self.assertEqual(self.data.num, 11111111111111)
            self.data.num = -1
            self.data.num
            self.assertEqual(self.data.num, -1)
            self.data.num = -2
            self.data.num
            self.assertEqual(self.data.num, -2)

        with self.assertRaises(Exception):
            self.data.num = True
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = False
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = 0.1
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = 199999999.0000000001
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = 'string'
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = []
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = [0]
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = [2, 2]
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = ['str']
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = {}
        self.assertEqual(self.data.num, -2)
        with self.assertRaises(Exception):
            self.data.num = {'string': 'str'}
        self.assertEqual(self.data.num, -2)

    def test_assign_name(self):
        with self.assertNotRaises():
            self.data.name = ''
            self.data.name
            self.assertEqual(self.data.name, '')
            self.data.name = 'asdf'
            self.data.name
            self.assertEqual(self.data.name, 'asdf')
            self.data.name = '12'
            self.data.name
            self.assertEqual(self.data.name, '12')
            self.data.name = 'df sdf sdf'
            self.data.name
            self.assertEqual(self.data.name, 'df sdf sdf')

        with self.assertRaises(Exception):
            self.data.name = 0
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = 1
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = -1
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = []
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = [0]
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = [2, 2]
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = ['str']
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = {}
        self.assertEqual(self.data.name, 'df sdf sdf')
        with self.assertRaises(Exception):
            self.data.name = {'string': 'str'}
        self.assertEqual(self.data.name, 'df sdf sdf')

    def test_assign_price(self):
        with self.assertNotRaises():
            self.data.price = 1
            self.data.price
        self.assertEqual(self.data.price, 1)
        with self.assertNotRaises():
            self.data.price = 2
            self.data.price
        self.assertEqual(self.data.price, 2)
        with self.assertNotRaises():
            self.data.price = 10000
            self.data.price
        self.assertEqual(self.data.price, 10000)
        with self.assertNotRaises():
            self.data.price = 500
            self.data.price
        self.assertEqual(self.data.price, 500)
        with self.assertNotRaises():
            self.data.price = 11111111111111
            self.data.price
        self.assertEqual(self.data.price, 11111111111111)

        with self.assertRaises(Exception):
            self.data.price = 0
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = -1
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = -123123123
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = 'string'
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = []
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = [0]
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = [2, 2]
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = ['str']
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = {}
        self.assertEqual(self.data.price, 11111111111111)
        with self.assertRaises(Exception):
            self.data.price = {'string': 'str'}
        self.assertEqual(self.data.price, 11111111111111)
