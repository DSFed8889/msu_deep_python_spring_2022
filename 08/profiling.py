import sys
import weakref
import cProfile
import pstats
import io
import time

from LRU_cache import LRUCache
from memory_profiler import profile


class A:
    def __init__(self, i, j):
        self.num = i**j

    def __del__(self):
        time.sleep(2)


class ObInf:
    def __init__(self, ob):
        self.ob = ob
        self.init_refs_count = sys.getrefcount(self.ob) - 1
        self.ob_size = sys.getsizeof(self.ob)


class ObInfSlots:
    __slots__ = ('ob', 'weak_ref', 'init_refs_count', 'ob_size',)

    def __init__(self, ob):
        self.ob = ob
        self.init_refs_count = sys.getrefcount(self.ob) - 1
        self.ob_size = sys.getsizeof(self.ob)


def set_cache():
    cache = LRUCache(7)
    a = A(10000, 100)
    print('Created A class object. Refs more by 2 from real because of profile wrapper ref and function call stack ref')
    print('a refs: ', sys.getrefcount(a) - 1)
    for i in range(100):
        cache.set(f'a {i} ref', a)
    print('a refs after filling of cache: ', sys.getrefcount(a) - 1)
    cache.set('a weak ref', weakref.ref(a))
    print('a refs after creating a weak ref: ', sys.getrefcount(a) - 1)
    time.sleep(1)
    cache.set('ObInf', [ObInf({f'str {i}'}) for i in range(50_000)])
    cache.set('Slot ObInf', [ObInfSlots({f'str {i}'}) for i in range(50_000)])
    print('a refs at and of cache set: ', sys.getrefcount(a) - 1)
    return cache


@profile
def mem_profile():
    cache = set_cache()
    print('Object A: ', cache.get('a weak ref'),
          '\n\tRefs to it: ', sys.getrefcount(cache.get('a weak ref')()) - 1)
    for i in range(4):
        cache.set(i, f'{i} value')
    print('Object A: ', cache.get('a weak ref'))
    cache.set('del ObInf', 0)
    cache.clear()
    del cache
    print('Memory profile end!')


pr = cProfile.Profile()
pr.enable()

mem_profile()

pr.disable()


out = io.StringIO()
ps = pstats.Stats(pr, stream=out)
ps.print_stats()

print(out.getvalue())
