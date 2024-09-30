""" In this calculator model in the first step, 
we defined 4 different functions: add, subtract, multiply, and divide.
They will return the result."""

# Add two numbers
def add(num1: float, num2: float) -> float:
    result = num1 + num2   
    return result

# Subtract num2 from num1
def subtract(num1: float, num2: float) -> float:
    return num1 - num2

# Multiply num1 and num2
def multiply(num1: float, num2: float) -> float:
    return num1 * num2

# Divide num1 by num2
def divide(num1: float, num2: float) -> float:
    if num2 != 0:
        return num1 / num2
    else:  #handling the error due to division by zero.
        raise ValueError("Division by zero is not allowed") 

"""  The main calculator function is a true while loop that will use 
other functions."""
def calculator():
    print("\nWelcome to the Calculator!")

    while True:
        #Options panel
        print("\nChoose an operation:")
        print("\n1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("\n5. Exit")

        option = input("Enter your choice (1-5): ") #chosing one of options with user input
        #the first option "5" always will be break the loop befor any process 
        if option == '5':
            print("Exiting the calculator. Goodbye!")
            break

         # Try block to handle input validation type
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
         # exception will run in case of any problem in the inputs   
        except ValueError:
            print("Error: Please enter valid numeric values.")
            # this will avoid of break in program by going into the beginig of the while loop
            continue   

            # Perform selected operation based on user's choice
        if option == '1':
            result = add(num1, num2)
            print(f"Result of {num1} + {num2} = {result}")
        elif option == '2':
            result = subtract(num1, num2)
            print(f"Result of {num1} - {num2} = {result}")
        elif option == '3':
            result = multiply(num1, num2)
            print(f"Result of {num1} * {num2} = {result}")
        elif option == '4':
            try:
                result = divide(num1, num2)
                print(f"Result of {num1} / {num2} = {result}")
            except ValueError as e:
                print(str(e))
        else:
            print("Error: Invalid option. Please enter a valid choice (1-5).")

# Run the Calculator by calling the function
calculator()
