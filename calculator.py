def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Zero division error"
    return a / b


# Start infinity loop that keeps calculator running until user exits
while True:
    print("\nSelect operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("Type 'exit' to quit")

    choice = input("Enter Your choice (1/2/3/4): ")

    if choice.lower() == "exit":
        print("Thanks for using the calculator. Goodbye!")
        break

    # Check if choice is valid
    if choice in ("1", "2", "3", "4"):
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == "1":
            print(f"Result: {a} + {b} = {add(a, b)}")
        elif choice == "2":
            print(f"Result: {a} - {b} = {sub(a, b)}")
        elif choice == "3":
            print(f"Result: {a} * {b} = {multiply(a, b)}")
        elif choice == "4":
            result = division(a, b)
            if result == "Zero division error":
                print(result)
            else:
                print(f"Result: {a} / {b} = {result}")
    else:
        print("Invalid Input. Please choose a number from 1 to 4.")