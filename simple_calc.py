#test for git

# lists
known_operators = ["+", "-", "*", "/", "%"]

# welcome screen
print("""\n welcome to RJ's simple calculator!! """ )

# exit loop
while True:
    exitchoice = str(input("press enter to continue or type 'quit' to exit: "))

    if exitchoice == "quit":
        print("Goodbye!")
        exit()

    elif exitchoice == "":
        # getting user input for first number
        num1 = float(input("Enter first number: "))

        # operator help/unknow loop
        while True:

            # getting user input for the operator
            operand = input("Enter operator type 'help' for a list of all available operators: ")

            if operand == "help":
                print(known_operators)
            elif operand in known_operators:
                break

            else:
                print("Please enter a valid operator")

        # getting user input for second number
        num2 = float(input("Enter second number: "))

        # output
        if operand == "+":
            print(num1 + num2)
        elif operand == "-":
            print(num1 - num2)
        elif operand == "*":
            print(num1 * num2)
        elif operand == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
            else:
                print(num1 / num2)
        elif operand == "%":
            print(num1 % num2)


    else:
        print("unknown command")





