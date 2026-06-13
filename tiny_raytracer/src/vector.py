import math


class Vector:
    # TODO: Implement constructor
    def __init__(self, *args):
        self.components: list[float] = [n for n in args]
        self.size = len(self.components)
        # for n in args:
        #     self.components.append(n)

    # TODO: Implement __str__

    # TODO: Implement properties

    # TODO: Implement dot product

    # TODO: Implement norm

    # TODO: Implement normalize

    # TODO: Implement cross product

    def __add__(self, other):
        if self.size != other.size:
            raise ValueError

        new_components = []
        for n in range(self.size):
            new_components.append(self.components[n] + other.components[n])
        return Vector(*new_components)

    # TODO: Implement __sub__ (subtraction)

    # TODO: Implement division (which special function name is the correct one?)

    # TODO: Implement __mul__ (multiplication)

    # TODO: Try vector * scalar and scalar * vector

    # TODO: Implement __neg__ (additive inverse)

    # TODO: Implement __eq__
    def __eq__(self, other):
        if self.size != other.size:
            return False

        for n in range(self.size):
            if self.components[n] != other.components[n]:
                return False

        return True

    # TODO: Implement __getitem__

    pass
