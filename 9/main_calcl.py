from  moduless.input_module import get_numbers
from moduless.processing_module import add,minus,multiply,divide
from moduless.output_module import print_result, log_result
def main():
    log_file = "calculations.txt"
    num1, num2 = get_numbers()
    operations = {
    "sum": add(num1, num2),
    "minus": minus(num1, num2),
    "multiply": multiply(num1, num2),
    "divide": divide(num1, num2)
}

    for operation, result in operations.items():
        print_result(operation,result)
        log_result(log_file,operation,result)

if __name__ == "__main__":
    main()