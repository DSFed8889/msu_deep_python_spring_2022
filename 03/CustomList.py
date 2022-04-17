class CustomList(list):
    def __sub__(self, other):
        add_len = len(self) - len(other)
        if add_len < 0:
            self += [0] * (-add_len)
        elif add_len > 0:
            other += [0] * add_len
        result = [0] * len(self)
        for i, elem in enumerate(self):
            result[i] = elem - other[i]
        if add_len < 0:
            self = self[:add_len]
        elif add_len > 0:
            other = other[:-add_len]
        return CustomList(result)

    def __rsub__(self, other):
        add_len = len(self) - len(other)
        if add_len < 0:
            self += [0] * (-add_len)
        elif add_len > 0:
            other += [0] * add_len
        result = [0] * len(self)
        for i, elem in enumerate(other):
            result[i] = elem - self[i]
        if add_len < 0:
            self = self[:add_len]
        elif add_len > 0:
            other = other[:-add_len]
        return CustomList(result)

    def __add__(self, other):
        add_len = len(self) - len(other)
        if add_len < 0:
            self += [0] * (-add_len)
        elif add_len > 0:
            other += [0] * add_len
        result = [0] * len(self)
        for i, elem in enumerate(self):
            result[i] = elem + other[i]
        if add_len < 0:
            self = self[:add_len]
        elif add_len > 0:
            other = other[:-add_len]
        return CustomList(result)

    def __radd__(self, other):
        add_len = len(self) - len(other)
        if add_len < 0:
            self += [0] * (-add_len)
        elif add_len > 0:
            other += [0] * add_len
        result = [0] * len(self)
        for i, elem in enumerate(self):
            result[i] = elem + other[i]
        if add_len < 0:
            self = self[:add_len]
        elif add_len > 0:
            other = other[:-add_len]
        return CustomList(result)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        result = "["
        for i in self:
            result += str(i) + ", "
        result += "sum=" + str(sum(self)) + "]"
        return result
