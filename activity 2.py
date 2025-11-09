try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("result is : ", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: please enter numerical values only.")
except NameError as ex:
    print("The exception is:", ex)
    print("An unexpected error occurred:", ex)
finally:
    print("Execution completed.")