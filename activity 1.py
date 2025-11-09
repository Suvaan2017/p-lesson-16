try:
    number = int(input("Enter an number: "))
    print(f"You entered: {number}")
except ValueError as ex:
    print ("expception:", ex)
