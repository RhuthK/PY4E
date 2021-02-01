#Write a program to prompt the user for hours and
# rate per hour to compute gross pay

hours = int(input("Enter number of hours:   "))
rate = float(input("Enter rate per hour :   "))
total_pay = hours * rate
print("total pay is : ", total_pay)
