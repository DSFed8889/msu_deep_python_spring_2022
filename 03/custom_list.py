class CustomList(list):
    def __sub__(self, other):
        result = [0] * max(len(self), len(other))
        if len(self) - len(other) > 0:
            for i, elem in enumerate(other):
                result[i] = self[i] - elem
            for i, elem in enumerate(self[len(other):], start=len(other)):
                result[i] = elem
        else:
            for i, elem in enumerate(self):
                result[i] = elem - other[i]
            for i, elem in enumerate(other[len(self):], start=len(self)):
                result[i] = -elem
        return CustomList(result)

    def __rsub__(self, other):
        result = [0] * max(len(self), len(other))
        if len(self) - len(other) > 0:
            for i, elem in enumerate(other):
                result[i] = elem - self[i]
            for i, elem in enumerate(self[len(other):], start=len(other)):
                result[i] = -elem
        else:
            for i, elem in enumerate(self):
                result[i] = other[i] - elem
            for i, elem in enumerate(other[len(self):], start=len(self)):
                result[i] = elem
        return CustomList(result)

    def __add__(self, other):
        result = [0] * max(len(self), len(other))
        if (len(self) - len(other)) > 0:
            for i, elem in enumerate(other):
                result[i] = self[i] + elem
            for i, elem in enumerate(self[len(other):], start=len(other)):
                result[i] = elem
        else:
            for i, elem in enumerate(self):
                result[i] = elem + other[i]
            for i, elem in enumerate(other[len(self):], start=len(self)):
                result[i] = elem
        return CustomList(result)

    def __radd__(self, other):
        result = [0] * max(len(self), len(other))
        if len(self) - len(other) > 0:
            for i, elem in enumerate(other):
                result[i] = self[i] + elem
            for i, elem in enumerate(self[len(other):], start=len(other)):
                result[i] = elem
        else:
            for i, elem in enumerate(self):
                result[i] = elem + other[i]
            for i, elem in enumerate(other[len(self):], start=len(self)):
                result[i] = elem
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
