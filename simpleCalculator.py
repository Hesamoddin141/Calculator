# a Simple Calculator

print("the Simple Calculator!")
# make a interface to choose by user 

while True:         #making the whole calcaurator in a big loop it will be always true
    print("\n   choose one of options 1 to 5:")   # this section will just show the list of options to user
    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    option = input("Enter one of option 1 to 5: ") # getting input to using the right option,using operator or breaking the loop

    if option == '5':         # we need to use the exit case at the first step to avoid delay 
        print("Exiting ,Goodbye!")
        break                   # exit, and breaking the loop

    num1 = input("Enter first number: ")       # getting inputs for first number
    num2 = input("Enter second number: ")      # getting inputs for second number

    # making sure that input got the right type ,it is better to use float ratter then int for better accurcy in results
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error. Please enter only numbers!!!")
       # continue      # it will be go at the bigening of the loop
       # using of a if condition to find the user input option
    if option == '1': # interface for adding
        sum = num1 + num2
        print("Result:", sum)
    elif option == '2':  # interface for subtract
        sub = num1 - num2
        print("Result:", sub)
    elif option == '3':     # interface for multiplcation
        mul = num1 * num2
        print("Result:", mul)
    elif option == '4':    # interface for diviation
        if num2 != 0:      # we need to check for avoid of error num/0
            div = num1 / num2
            print("Result:", div)
        else:
            print("Error ,divided by zero :( ")  # to show a message in case of error
    else:
        print("Please enter a valid option (1-5)") # we cover all numbers 1 to 5 so if user choose anything else well see this message

