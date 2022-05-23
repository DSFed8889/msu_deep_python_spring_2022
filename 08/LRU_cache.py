class LRUCache:
    def __init__(self, limit=42):
        if type(limit) is not int:
            raise TypeError('Limit must be int type!')
        if limit < 0:
            raise ValueError('Limit must be non negative!')
        self.limit = limit
        self._data = {}
        self.__LRU = []

    def get(self, key):
        if key in self._data:
            self.__LRU.pop(self.__LRU.index(key))
            self.__LRU.append(key)
            return self._data[key]

    def __getitem__(self, item):
        return self.get(item)

    def set(self, key, value):
        if key in self._data:
            self.__LRU.pop(self.__LRU.index(key))
        if len(self.__LRU) == self.limit and self.limit != 0:
            self._data.pop(self.__LRU[0])
            self.__LRU = self.__LRU[1:]
        self.__LRU.append(key)
        self._data[key] = value

    def __setitem__(self, key, value):
        self.set(key, value)

    def clear(self):
        self._data = {}
        self.__LRU = []
