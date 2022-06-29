# Simple CLI Calculator
from ast import Continue

from zmq import MORE


print("Welcome To Simple CLI Calculator")

is_running = True

while is_running:
    # Processing Calculations...
    
    user_operation = input("what operation would you like to perform? \nPick any of : ['+','-','/','*','%' ] : ")
    
    # Get user number
    try: # Try to get user input values , if the values are floats, continue 
        number1 = float(input("First number: "))
        number2 = float(input("Second number: "))
    
    except: #When we get an error while running
        print("Failed, Invalid numbers...")
        Continue

    if user_operation == "+": 
        # perform addition
        print(number1 + number2)

    elif user_operation == "*":
        # perform multiplicaion
        print(number1 * number2)
   
    elif user_operation == "/":
        # perform division
        print(number1 / number2)
   
    elif user_operation == "%":
        #perfom modulation
        print(number1 % number2)

    elif user_operation == "- ":
        # perform subtraction 
        print(number1 - number2)

    else:
        # Invalid operation
        print("Invalid operation entered, try again...")
    
    more = input("Would you like to perform another calculation. [yes,no]")
    if more == "yes":
        pass
    
    if more == "no":
        is_running = False
        # This is the same thing as a break.
        
print("End of calculations")
# Ctrl + C to exit any Python program...!