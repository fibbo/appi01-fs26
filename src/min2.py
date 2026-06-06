def min2(*args):
    if len(args) < 2:
        return "No second smallest value exist."

    # Ternary expression => x = value_if_true if some_condition else value_if_false
    min, min2 = (args[0], args[1]) if args[0] < args[1] else (args[1], args[0])

    for n in args[2:]:
        if n < min:
            min2 = min
            min = n
        elif n < min2:
            min2 = n
    return min2


if __name__ == "__main__":
    print(min2(-1, 2, 3, -34, 5, 2, 0, 2))
