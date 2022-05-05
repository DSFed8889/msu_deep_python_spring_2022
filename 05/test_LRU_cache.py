import unittest
from LRU_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_no_limt(self):
        cache = LRUCache(limit=0)
        for i in range(10000):
            self.assertEqual(cache.get(f'key1_{i}'), None)
        for i in range(10000):
            cache.set(f'key1_{i}', i)
        for i in range(10000):
            self.assertEqual(cache.get(f'key1_{i}'), i)
        for i in range(10000):
            cache.set(f'key1_{i}', 200000)
        for i in range(10000):
            self.assertEqual(cache.get(f'key1_{i}'), 200000)
        for i in range(10000):
            self.assertEqual(cache[f'key2_{i}'], None)
        for i in range(10000):
            cache[f'key2_{i}'] = i
        for i in range(10000):
            self.assertEqual(cache[f'key2_{i}'], i)
        for i in range(10000):
            cache[f'key2_{i}'] = 200000
        for i in range(10000):
            self.assertEqual(cache[f'key2_{i}'], 200000)

    def test_LRU(self):
        cache = LRUCache(5)
        for i in range(5):
            self.assertEqual(cache[f'k{i}'], None)
            cache[f'k{i}'] = [i] * (i + 1)
        for i in range(5):
            self.assertEqual(cache[f'k{i}'], [i] * (i + 1))
        cache['k5'] = 'five'
        self.assertEqual(cache['k0'], None)
        for i in range(1, 5):
            self.assertEqual(cache[f'k{i}'], [i] * (i + 1))
        self.assertEqual(cache['k5'], 'five')

        cache = LRUCache(5)
        for i in range(5):
            self.assertEqual(cache[f'k{i}'], None)
            cache[f'k{i}'] = [i] * (i + 1)
        for i in range(5):
            self.assertEqual(cache[f'k{5 - i - 1}'], [5 - i - 1] * (5 - i))
        cache['k5'] = 'five'
        self.assertEqual(cache['k4'], None)
        for i in range(4):
            self.assertEqual(cache[f'k{i}'], [i] * (i + 1))
        self.assertEqual(cache['k5'], 'five')

        cache = LRUCache(5)
        for i in range(5):
            self.assertEqual(cache[f'k{i}'], None)
            cache[f'k{i}'] = [i] * (i + 1)
        for i in range(5):
            self.assertEqual(cache[f'k{i}'], [i] * (i + 1))
        self.assertEqual(cache['k0'], [0])
        cache['k5'] = 'five'
        self.assertEqual(cache['k0'], [0])
        self.assertEqual(cache['k1'], None)
        for i in range(2, 5):
            self.assertEqual(cache[f'k{i}'], [i] * (i + 1))
        self.assertEqual(cache['k5'], 'five')

    def test_errors(self):
        with self.assertRaises(TypeError):
            LRUCache(True)
        with self.assertRaises(TypeError):
            LRUCache(False)
        with self.assertRaises(TypeError):
            LRUCache(4.6)
        with self.assertRaises(TypeError):
            LRUCache('sdfdfwk')
        with self.assertRaises(TypeError):
            LRUCache({'sdfdfwk': 3})
        with self.assertRaises(TypeError):
            LRUCache([8])
        with self.assertRaises(ValueError):
            LRUCache(-100)
        cache = LRUCache(0)
        a = ['my_list']
        with self.assertRaises(TypeError):
            cache[a]
        with self.assertRaises(TypeError):
            cache.get(a)
        with self.assertRaises(TypeError):
            cache[a] = 0
        with self.assertRaises(TypeError):
            cache.set(a, 0)

    def test_limit_1(self):
        cache = LRUCache(1)
        self.assertEqual(cache['key1'], None)
        self.assertEqual(cache['key2'], None)
        cache['key1'] = 1
        self.assertEqual(cache['key1'], 1)
        self.assertEqual(cache['key2'], None)
        cache['key2'] = 2
        self.assertEqual(cache['key1'], None)
        self.assertEqual(cache['key2'], 2)

    def test_full_refilling(self):
        cache = LRUCache(5)
        for i in range(5):
            self.assertEqual(cache[f'key{i}'], None)
            cache[f'key{i}'] = [i] * (i + 1)
        for i in range(5):
            self.assertEqual(cache[f'key{i}'], [i] * (i + 1))
        for i in range(8):
            cache[f'new_key{i}'] = f'new_key{i} value'
        for i in range(5):
            self.assertEqual(cache[f'key{i}'], None)
        for i in range(3):
            self.assertEqual(cache[f'new_key{i}'], None)
        for i in range(3, 8):
            self.assertEqual(cache[f'new_key{i}'], f'new_key{i} value')

    def test_homework_md(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

    def test_reset_value(self):
        cache = LRUCache(10)

        for i in range(10):
            self.assertEqual(cache[f'key{i}'], None)
            cache[f'key{i}'] = [i] * (i + 1)
        for i in range(10):
            self.assertEqual(cache[f'key{i}'], [i] * (i + 1))
        for i in range(5):
            self.assertEqual(cache[f'key{i}'], [i] * (i + 1))
        cache['key0'] = 'new_value'
        for i in range(9):
            cache[f'new_key{i}'] = [f'new_key{i}', 'value']
        for i in range(9):
            self.assertEqual(cache[f'new_key{i}'], [f'new_key{i}', 'value'])
        self.assertEqual(cache['key0'], 'new_value')
