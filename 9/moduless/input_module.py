def get_numbers():
    try:
        num1 = float(input("Enter the  first number: "))
        num2 = float(input("Enter the second number "))
        return num1, num2
    except ValueError:
        print("Invalid input")
        return get_numbers()