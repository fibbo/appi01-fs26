VALID_OPERATIONS = ("+", "-", "/", "*")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def main():
    while True:
        print("Please enter two numbers: ")
        try:
            a = None
            b = None
            a = input("First number: ")
            b = input("Second number: ")
            a = float(a)
            b = float(b)
        except ValueError:
            print(f"a and b must be numbers: {a, b}")
            continue
        op = input(f"Please select the operation ({VALID_OPERATIONS}): ")
        if op not in VALID_OPERATIONS:
            print(f"Invalid operation. Valid operations: {VALID_OPERATIONS}")
            continue

        match op:
            case "+":
                print(add(a, b))
            case "/":
                # if b == 0:
                #     return "Invalid: dividing by 0"
                try:
                    print(divide(a, b))
                except ZeroDivisionError:
                    return "Invalid: dividing by 0"

            case "*":
                print(multiply(a, b))
            case "-":
                print(subtract(a, b))

        # if op == "+":
        #     print(add(a, b))

        # print(eval(f"{a} {op} {b}"))

        again = input("Do you want to calculate something else? ([yes]/no) ")
        if again.lower() == "no":
            break


if __name__ == "__main__":
    main()
