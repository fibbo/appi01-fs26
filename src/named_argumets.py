def division(a, b):
    return a / b


def division2(p=1, q=1):
    return p / q


def example(x, b=7):
    pass


p = 7
print(division(8, 4))
print(division(4, 8))

print(division2(q=3, p=1))
print(division2(p=1, q=3))

print(division2())


example(4)
example(2, 8)
