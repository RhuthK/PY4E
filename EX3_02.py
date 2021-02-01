''' Rewrite your pay program using try and except so that your
program handles non-numeric input gracefully by printing a message
and exiting the program. '''

try:
    hours = int(input("Enter hours :  "))
    rate = float(input("Enter rate :  "))
    pay = hours  * rate
    print(pay)
except:
    print("Error, please enter numeric input")
    
