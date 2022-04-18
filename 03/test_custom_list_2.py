import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        print("Set up")

    def tearDown(self):
        print("Tear down")

    def test_sub_only_customs_1(self):
        list_1 = CustomList([])
        list_2 = CustomList([])
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 3)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([5, 1, 3, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 7]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([4, -1, -4, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0])
        list_2 = CustomList([0])
        test_list = list_1 - list_2
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

    def test_sub_only_customs_2(self):
        list_1 = CustomList([0, 0, 0, 0, 0])
        list_2 = CustomList([0, 0])
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
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

    def test_sub_only_customs_3(self):
        list_1 = CustomList([0, 0, 0])
        list_2 = CustomList([0, 0, 0, 0])
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([4]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 7, 8])
        list_2 = CustomList([1, 8])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([4, 5, 6, 7, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 8]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([3, -3, 6, 7, 8]):
            self.assertTrue(elem == test_list[i])

    def test_sub_only_customs_4(self):
        list_1 = CustomList([4, 5, 6, 7])
        list_2 = CustomList([1, 8])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 8]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([3, -3, 6, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = CustomList([10, 20, 1, 3, 5, 4, 0])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 1, 3, 5, 4, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, 5, -3, -5, -4, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = CustomList([10, 20, 10, 30])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 10, 30]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, -4, -30]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 8])
        list_2 = CustomList([10, 20, 10, 30])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 10, 30]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, -4, -22]):
            self.assertTrue(elem == test_list[i])

    def test_sub_list_l_1(self):
        list_1 = []
        list_2 = CustomList([])
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 3)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([5, 1, 3, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 7]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([4, -1, -4, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = [0]
        list_2 = CustomList([0])
        test_list = list_1 - list_2
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

    def test_sub_list_l_2(self):
        list_1 = [0, 0, 0, 0, 0]
        list_2 = CustomList([0, 0])
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
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

    def test_sub_list_l_3(self):
        list_1 = [0, 0, 0]
        list_2 = CustomList([0, 0, 0, 0])
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([4]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6, 7, 8]
        list_2 = CustomList([1, 8])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([4, 5, 6, 7, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 8]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([3, -3, 6, 7, 8]):
            self.assertTrue(elem == test_list[i])

    def test_sub_list_l_4(self):
        list_1 = [4, 5, 6, 7]
        list_2 = CustomList([1, 8])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 8]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([3, -3, 6, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6]
        list_2 = CustomList([10, 20, 1, 3, 5, 4, 0])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 1, 3, 5, 4, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, 5, -3, -5, -4, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6]
        list_2 = CustomList([10, 20, 10, 30])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 10, 30]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, -4, -30]):
            self.assertTrue(elem == test_list[i])

        list_1 = [4, 5, 6, 8]
        list_2 = CustomList([10, 20, 10, 30])
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 10, 30]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, -4, -22]):
            self.assertTrue(elem == test_list[i])

    def test_sub_list_r_1(self):
        list_1 = CustomList([])
        list_2 = []
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 3)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([5, 1, 3, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 2, 7]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([4, -1, -4, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([0])
        list_2 = [0]
        test_list = list_1 - list_2
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

    def test_sub_list_r_2(self):
        list_1 = CustomList([0, 0, 0, 0, 0])
        list_2 = [0, 0]
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
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

    def test_sub_list_r_3(self):
        list_1 = CustomList([0, 0, 0])
        list_2 = [0, 0, 0, 0]
        test_list = list_1 - list_2
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
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 1)
        self.assertEqual(len(list_2), 1)
        self.assertEqual(len(test_list), 1)
        for i, elem in enumerate([4]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([2]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 7, 8])
        list_2 = [1, 8]
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 5)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 5)
        for i, elem in enumerate([4, 5, 6, 7, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 8]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([3, -3, 6, 7, 8]):
            self.assertTrue(elem == test_list[i])

    def test_sub_list_r_4(self):
        list_1 = CustomList([4, 5, 6, 7])
        list_2 = [1, 8]
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 2)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 7]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([1, 8]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([3, -3, 6, 7]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = [10, 20, 1, 3, 5, 4, 0]
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 7)
        self.assertEqual(len(test_list), 7)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 1, 3, 5, 4, 0]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, 5, -3, -5, -4, 0]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6])
        list_2 = [10, 20, 10, 30]
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 3)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 10, 30]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, -4, -30]):
            self.assertTrue(elem == test_list[i])

        list_1 = CustomList([4, 5, 6, 8])
        list_2 = [10, 20, 10, 30]
        test_list = list_1 - list_2
        self.assertIsInstance(test_list, CustomList)
        self.assertEqual(len(list_1), 4)
        self.assertEqual(len(list_2), 4)
        self.assertEqual(len(test_list), 4)
        for i, elem in enumerate([4, 5, 6, 8]):
            self.assertTrue(elem == list_1[i])
        for i, elem in enumerate([10, 20, 10, 30]):
            self.assertTrue(elem == list_2[i])
        for i, elem in enumerate([-6, -15, -4, -22]):
            self.assertTrue(elem == test_list[i])
