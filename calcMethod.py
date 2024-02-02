def get_operand(word_number):
    return int(input(f"Please enter the {word_number} whole number: "))

if __name__ == "__main__":
    num1 = get_operand("first")
    num2 = get_operand("second")

    while True:
        print("""
            What operation would you like to conduct with the 2 numbers provided?
            + - addition
            - - subtraction
            * - multiplication
            / - division
            % - modulus""")
        
        operation_selection = input().strip()[0]

        if operation_selection not in {'+', '-', '*', '/', '%'}:
            print("Invalid Selection!")
            continue

        if operation_selection == '+':
            result = num1 + num2
            print("Option selected: --> +\n")
            print(f"The result of adding {num1} to {num2} is {result}")

        elif operation_selection == '-':
            result = num1 - num2
            print("Option selected: --> -\n")
            print(f"The result of subtracting {num2} from {num1} is {result}")

        elif operation_selection == '*':
            result = num1 * num2
            print("Option selected: --> *\n")
            print(f"The result of multiplying {num1} by {num2} is {result}")

        elif operation_selection == '/':
            print("Option selected: --> /\n")
            if num2 == 0:
                print("Value Error, Division by 0 is not possible, Goodbye!")
            else:
                print(f"The result of dividing {num1} by {num2} is {num1 / num2:.2f}")

        elif operation_selection == '%':
            print("Option selected: --> %\n")
            if num2 == 0:
                print("Value Error, Modulo division does not allow division by zero, Goodbye!")
            else:
                print(f"The result of {num1} modulus {num2} is {num1 % num2}")

        break


