while True:
    first_number = float(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    second_number = float(input("Enter the second number: "))

    if operation == "+":
        print("Result:", first_number + second_number)

    elif operation == "-":
        print("Result:", first_number - second_number)

    elif operation == "*":
        print("Result:", first_number * second_number)

    elif operation == "/":
        if second_number == 0:
            print("Division by zero is not allowed.")
        else:
            print("Result:", first_number / second_number)

    else:
        print("Invalid operation.")

    answer = input("Do you want to continue? (yes/y): ")

    if answer.lower() != "yes" and answer.lower() != "y":
        break