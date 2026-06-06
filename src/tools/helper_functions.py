def square_root(x):
    """Returns the square root of a number."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    return x**0.5


def addition(*args):
    result = 0
    for n in args:
        result += n
    return result


if __name__ == "__main__":
    print(addition(2, 3, 4))
