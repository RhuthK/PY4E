# Write a proggram which repeatedly reads numbers until the user enters 'done' .
# Once done is enteres, print out the total, count , and average of the numbers
# if the user enters anything other than a number , detect using try
# and except and print an error message and skip to the next number


count = 0
total = 0
average = 0 
while True: 
    num = input('Enter a number : ')
    if str(num) == 'done':
        break
    try:
        numInt = int(num)
    except :
        print('invalid input')
        continue
    total += numInt
    count += 1
    average = total / count 
            

print(total, count, average)

        
    

    
    
    
        

