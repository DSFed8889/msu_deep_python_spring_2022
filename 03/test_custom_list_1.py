import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        print("Set up")

    def tearDown(self):
        print("Tear down")

    def test_add_only_customs_1(self):
        list_1 = CustomList([])
        list_2 = CustomList([])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 0)
        self.assertEqual(len(list_2), 0)
        self.assertEqual(len(test_list), 0)
        for i, elem in enumerate([]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([5, 1, 3, 7])
        list_2 = CustomList([1, 2, 7])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 3)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([5, 1, 3, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 7]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([6, 3, 10, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0])
        list_2 = CustomList([0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0]):
            self.assertTrue(elem == test_list[i])

    def test_add_only_customs_2(self):
        list_1 = CustomList([0, 0, 0, 0, 0])
        list_2 = CustomList([0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([0, 0, 0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0, 0, 0, 0])
        list_2 = CustomList([0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0, 0, 0])
        list_2 = CustomList([0, 0, 0, 0, 0, 0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0, 0, 0, 0, 0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

    def test_add_only_customs_3(self):
        list_1 = CustomList([0, 0, 0])
        list_2 = CustomList([0, 0, 0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4])
        list_2 = CustomList([2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([4]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([6]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 7, 8])
        list_2 = CustomList([1, 2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([4, 5, 6, 7, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 6, 7, 8]):
            self.assertTrue(elem == test_list[i])

    def test_add_only_customs_4(self):
        list_1 = CustomList([4, 5, 6, 7])
        list_2 = CustomList([1, 2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 6, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = CustomList([1, 2, 1, 3, 5, 4, 2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3, 5, 4, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 3, 5, 4, 2]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = CustomList([1, 2, 1, 3])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 3]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 8])
        list_2 = CustomList([1, 2, 1, 3])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 11]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_l_1(self):
        list_1 = []
        list_2 = CustomList([])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 0)
        self.assertEqual(len(list_2), 0)
        self.assertEqual(len(test_list), 0)
        for i, elem in enumerate([]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([]):
            self.assertTrue(elem == test_list[i])

        list_1 = [5, 1, 3, 7]
        list_2 = CustomList([1, 2, 7])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 3)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([5, 1, 3, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 7]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([6, 3, 10, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = [0]
        list_2 = CustomList([0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_l_2(self):
        list_1 = [0, 0, 0, 0, 0]
        list_2 = CustomList([0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([0, 0, 0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = [0, 0, 0, 0]
        list_2 = CustomList([0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = [0, 0, 0]
        list_2 = CustomList([0, 0, 0, 0, 0, 0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0, 0, 0, 0, 0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_l_3(self):
        list_1 = [0, 0, 0]
        list_2 = CustomList([0, 0, 0, 0])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4]
        list_2 = CustomList([2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([4]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([6]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6, 7, 8]
        list_2 = CustomList([1, 2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([4, 5, 6, 7, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 6, 7, 8]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_l_4(self):
        list_1 = [4, 5, 6, 7]
        list_2 = CustomList([1, 2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 6, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6]
        list_2 = CustomList([1, 2, 1, 3, 5, 4, 2])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3, 5, 4, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 3, 5, 4, 2]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6]
        list_2 = CustomList([1, 2, 1, 3])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 3]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6, 8]
        list_2 = CustomList([1, 2, 1, 3])
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 11]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_r_1(self):
        list_1 = CustomList([])
        list_2 = []
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 0)
        self.assertEqual(len(list_2), 0)
        self.assertEqual(len(test_list), 0)
        for i, elem in enumerate([]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([5, 1, 3, 7])
        list_2 = [1, 2, 7]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 3)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([5, 1, 3, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 7]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([6, 3, 10, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0])
        list_2 = [0]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_r_2(self):
        list_1 = CustomList([0, 0, 0, 0, 0])
        list_2 = [0, 0]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([0, 0, 0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0, 0, 0, 0])
        list_2 = [0, 0]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0, 0, 0])
        list_2 = [0, 0, 0, 0, 0, 0, 0]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0, 0, 0, 0, 0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_r_3(self):
        list_1 = CustomList([0, 0, 0])
        list_2 = [0, 0, 0, 0]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([0, 0, 0]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([0, 0, 0, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4])
        list_2 = [2]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([4]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([6]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 7, 8])
        list_2 = [1, 2]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([4, 5, 6, 7, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 6, 7, 8]):
            self.assertTrue(elem == test_list[i])

    def test_add_list_r_4(self):
        list_1 = CustomList([4, 5, 6, 7])
        list_2 = [1, 2]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 6, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = [1, 2, 1, 3, 5, 4, 2]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3, 5, 4, 2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 3, 5, 4, 2]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = [1, 2, 1, 3]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 3]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 8])
        list_2 = [1, 2, 1, 3]
        test_list = list_1 + list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 1, 3]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([5, 7, 7, 11]):
            self.assertTrue(elem == test_list[i])

    def test_eq_rels_1(self):
        list_1 = CustomList([])
        list_2 = CustomList([])
        self.assertFalse(list_1 < list_2)
        self.assertTrue(list_1 <= list_2)
        self.assertTrue(list_1 == list_2)
        self.assertFalse(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertFalse(list_1 > list_2)

        list_1 = CustomList([0])
        list_2 = CustomList([])
        self.assertFalse(list_1 < list_2)
        self.assertTrue(list_1 <= list_2)
        self.assertTrue(list_1 == list_2)
        self.assertFalse(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertFalse(list_1 > list_2)

        list_1 = CustomList([0, 0, 0])
        list_2 = CustomList([0])
        self.assertFalse(list_1 < list_2)
        self.assertTrue(list_1 <= list_2)
        self.assertTrue(list_1 == list_2)
        self.assertFalse(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertFalse(list_1 > list_2)

        list_1 = CustomList([1])
        list_2 = CustomList([])
        self.assertFalse(list_1 < list_2)
        self.assertFalse(list_1 <= list_2)
        self.assertFalse(list_1 == list_2)
        self.assertTrue(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertTrue(list_1 > list_2)

        list_1 = CustomList([1, 0, 0])
        list_2 = CustomList([0, 1, 0])
        self.assertFalse(list_1 < list_2)
        self.assertTrue(list_1 <= list_2)
        self.assertTrue(list_1 == list_2)
        self.assertFalse(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertFalse(list_1 > list_2)

        list_1 = CustomList([2])
        list_2 = CustomList([0, 1, 1])
        self.assertFalse(list_1 < list_2)
        self.assertTrue(list_1 <= list_2)
        self.assertTrue(list_1 == list_2)
        self.assertFalse(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertFalse(list_1 > list_2)

    def test_eq_rels_2(self):
        list_1 = CustomList([2])
        list_2 = CustomList([])
        self.assertFalse(list_1 < list_2)
        self.assertFalse(list_1 <= list_2)
        self.assertFalse(list_1 == list_2)
        self.assertTrue(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertTrue(list_1 > list_2)

        list_1 = CustomList([])
        list_2 = CustomList([4])
        self.assertTrue(list_1 < list_2)
        self.assertTrue(list_1 <= list_2)
        self.assertFalse(list_1 == list_2)
        self.assertTrue(list_1 != list_2)
        self.assertFalse(list_1 >= list_2)
        self.assertFalse(list_1 > list_2)

        list_1 = CustomList([5, 4, 3])
        list_2 = CustomList([1, 2, 1, 3, 0, 1])
        self.assertFalse(list_1 < list_2)
        self.assertFalse(list_1 <= list_2)
        self.assertFalse(list_1 == list_2)
        self.assertTrue(list_1 != list_2)
        self.assertTrue(list_1 >= list_2)
        self.assertTrue(list_1 > list_2)

        list_1 = CustomList([2, 5, 3, 6, 3])
        list_2 = CustomList([100, 0])
        self.assertTrue(list_1 < list_2)
        self.assertTrue(list_1 <= list_2)
        self.assertFalse(list_1 == list_2)
        self.assertTrue(list_1 != list_2)
        self.assertFalse(list_1 >= list_2)
        self.assertFalse(list_1 > list_2)

    def test_str(self):
        lst = CustomList([])
        self.assertEqual(str(lst), "[sum=0]")

        lst = CustomList([0])
        self.assertEqual(str(lst), "[0, sum=0]")

        lst = CustomList([1, 0])
        self.assertEqual(str(lst), "[1, 0, sum=1]")

        lst = CustomList([2, 10086, 1])
        self.assertEqual(str(lst), "[2, 10086, 1, sum=10089]")

        lst = CustomList([0, 1, 4, 894, 352, 645])
        self.assertEqual(str(lst), "[0, 1, 4, 894, 352, 645, sum=1896]")
