import math


class Vector:
    # TODO: Implement constructor
    def __init__(self, *args):
        self.components: list[float] = [n for n in args]
        self.size = len(self.components)
        # for n in args:
        #     self.components.append(n)

    # TODO: Implement __str__

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def z(self):
        if self.size < 3:
            print("z property doesn't exist on a vector with less then 3 dimensions.")
        return self[2]

    # TODO: Implement dot product

    # TODO: Implement norm

    # TODO: Implement normalize

    # TODO: Implement cross product

    def __add__(self, other):
        if self.size != other.size:
            raise ValueError

        new_components = []
        for n in range(self.size):
            new_components.append(self[n] + other[n])
        return Vector(*new_components)

    def __sub__(self, other):
        if self.size != other.size:
            raise ValueError
        return self + -other

    # TODO: Implement division (which special function name is the correct one?)

    # TODO: Implement __mul__ (multiplication)

    # TODO: Try vector * scalar and scalar * vector

    def __neg__(self):
        # return Vector(*[-n for n in self.components])
        new_components = []
        for n in range(self.size):
            new_components.append(-self[n])
        return Vector(*new_components)

    def __eq__(self, other):
        if self.size != other.size:
            return False

        for n in range(self.size):
            if self[n] != other[n]:
                return False

        return True

    def __getitem__(self, key):
        if self.size <= key:
            raise IndexError
        return self.components[key]

    pass
