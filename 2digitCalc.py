if __name__ == "__main__":
    first_number = int(input("Please enter the first whole number: "))      #first number input
    second_number = int(input("Please enter the second whole number: "))    #second number input

    print("What operation would you like to conduct with the 2 numbers provided?\n"
          "1 - addition\n"
          "2 - subtraction\n"
          "3 - multiplication\n"
          "4 - division\n"
          "5 - modulus")
    operation_selection = int(input("Enter the number corresponding to the desired operation: "))

    if operation_selection == 1:
        result = first_number + second_number
        print("Option selected: --> 1\n")
        print(f"The result of adding {first_number} to {second_number} is {result}")
    elif operation_selection == 2:
        result = first_number - second_number
        print("Option selected: --> 2\n")
        print(f"The result of subtracting {second_number} from {first_number} is {result}")
    elif operation_selection == 3:
        result = first_number * second_number
        print("Option selected: --> 3\n")
        print(f"The result of multiplying {first_number} by {second_number} is {result}")
    elif operation_selection == 4:
        print("Option selected: --> 4\n")
        if second_number == 0:
            print("Value Error, Division by 0 is not possible")
        else:
            double_result = first_number / second_number
            print(f"The result of dividing {first_number} by {second_number} is {double_result:.2f}")
    elif operation_selection == 5:
        print("Option selected: --> 5\n")
        if second_number == 0:
            print("Value Error, Modulo division does not allow division by zero, Goodbye!")
        else:
            result = first_number % second_number
            print(f"The result of {first_number} modulus {second_number} is {result}")
    else:
        print("Invalid selection, Goodbye!")
