import unittest
from CustomList import CustomList


class TestCustomList(unittest.TestCase):
    def setUp(self):
        print("Set up")

    def tearDown(self):
        print("Tear down")

    def test_add_only_customs(self):
        test_list = CustomList([]) + CustomList([])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([6, 3, 10, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0]) + CustomList([0])
        for i, elem in enumerate(CustomList([0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0, 0]) + CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0]) + CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) + CustomList([0, 0, 0, 0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) + CustomList([0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4]) + CustomList([2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([6])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7, 8]) + CustomList([1, 2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 6, 7, 8])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7]) + CustomList([1, 2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 6, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) + CustomList([1, 2, 1, 3, 5, 4, 2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 7, 3, 5, 4, 2])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) + CustomList([1, 2, 1, 3])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 7, 3])):
            self.assertTrue(elem == test_list[i])

    def test_sub_only_customs(self):
        test_list = CustomList([]) - CustomList([])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([4, -1, -4, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0]) - CustomList([0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0, 0]) - CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0]) - CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) - CustomList([0, 0, 0, 0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) - CustomList([0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4]) - CustomList([2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([2])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7, 8]) - CustomList([1, 8])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([3, -3, 6, 7, 8])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7]) - CustomList([1, 8])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([3, -3, 6, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) - CustomList([10, 20, 10, 30, 50, 40, 20])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([-6, -15, -4, -30, -50, -40, -20])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) - CustomList([10, 20, 10, 30])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([-6, -15, -4, -30])):
            self.assertTrue(elem == test_list[i])

    def test_add_list_r(self):
        test_list = CustomList([]) + []
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([5, 1, 3, 7]) + [1, 2, 7]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([6, 3, 10, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0]) + CustomList([0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0, 0]) + [0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0]) + [0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) + [0, 0, 0, 0, 0, 0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) + [0, 0, 0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4]) + CustomList([2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([6])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7, 8]) + [1, 2]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 6, 7, 8])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7]) + [1, 2]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 6, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) + [1, 2, 1, 3, 5, 4, 2]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 7, 3, 5, 4, 2])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) + [1, 2, 1, 3]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 7, 3])):
            self.assertTrue(elem == test_list[i])

    def test_add_list_l(self):
        test_list = [] + CustomList([])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([])):
            self.assertTrue(elem == test_list[i])

        test_list = [5, 1, 3, 7] + CustomList([1, 2, 7])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([6, 3, 10, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = [0] + CustomList([0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0, 0, 0] + CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0, 0] + CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0] + CustomList([0, 0, 0, 0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0] + CustomList([0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [4] + CustomList([2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([6])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6, 7, 8] + CustomList([1, 2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 6, 7, 8])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6, 7] + CustomList([1, 2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 6, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6] + CustomList([1, 2, 1, 3, 5, 4, 2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 7, 3, 5, 4, 2])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6] + CustomList([1, 2, 1, 3])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([5, 7, 7, 3])):
            self.assertTrue(elem == test_list[i])

    def test_sub_list_r(self):
        test_list = CustomList([]) - []
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([5, 1, 3, 7]) - [1, 2, 7]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([4, -1, -4, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0]) - [0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0, 0]) - [0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0, 0]) - [0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) - [0, 0, 0, 0, 0, 0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([0, 0, 0]) - [0, 0, 0, 0]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4]) - [2]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([2])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7, 8]) - [1, 8]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([3, -3, 6, 7, 8])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6, 7]) - [1, 8]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([3, -3, 6, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) - [10, 20, 10, 30, 50, 40, 20]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([-6, -15, -4, -30, -50, -40, -20])):
            self.assertTrue(elem == test_list[i])

        test_list = CustomList([4, 5, 6]) - [10, 20, 10, 30]
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([-6, -15, -4, -30])):
            self.assertTrue(elem == test_list[i])

    def test_sub_list_l(self):
        test_list = [] - CustomList([])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([])):
            self.assertTrue(elem == test_list[i])

        test_list = [5, 1, 3, 7] - CustomList([1, 2, 7])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([4, -1, -4, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = [0] - CustomList([0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0, 0, 0] - CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0, 0] - CustomList([0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0] - CustomList([0, 0, 0, 0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [0, 0, 0] - CustomList([0, 0, 0, 0])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([0, 0, 0, 0])):
            self.assertTrue(elem == test_list[i])

        test_list = [4] - CustomList([2])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([2])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6, 7, 8] - CustomList([1, 8])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([3, -3, 6, 7, 8])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6, 7] - CustomList([1, 8])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([3, -3, 6, 7])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6] - CustomList([10, 20, 10, 30, 50, 40, 20])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([-6, -15, -4, -30, -50, -40, -20])):
            self.assertTrue(elem == test_list[i])

        test_list = [4, 5, 6] - CustomList([10, 20, 10, 30])
        self.assertIsInstance(test_list, CustomList)
        for i, elem in enumerate(CustomList([-6, -15, -4, -30])):
            self.assertTrue(elem == test_list[i])

    def test_eq_rels(self):
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
