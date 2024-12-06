def print_result(operation, result):
    if result is not None:
        print(f"The result of {operation} is {result}")
    else:
        print(f"The result of {operation} is underfind")
def log_result(filename, operation, result):
    with open(filename, "a") as file:
        if result is not None:
            file.write(f"the {operation} result is {result}\n")
        else:
            file.write(f"The {operation} result is underfind")