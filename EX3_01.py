# Rewrite your pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40


hours = int(input("Enter hours : "))
rate = float(input("Enter rate:  "))

normal_pay = hours * rate 
if (hours > 40):
    pay = (40* rate) + ((hours-40)*(rate * 1.5))
    print(pay)


    


