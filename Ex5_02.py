''' Write another program that prompts for a list of numbers as above and
at the end prints out both the maximum and minimum of the numbers instead of
the average '''

#[80,35, 56,1,67,22, 32]


minNum = None
maxNum = None

while True:
    try: 
        num = input('input a number :')
        if num == 'done': break

        alist = []
        alist.append(num)
        for element in alist:
            if minNum is None or element < minNum :
                minNum = element
            if maxNum is None or element > maxNum:
                maxNum = element
            
    except :
        print('invalid input')
        continue



print(minNum)
print(maxNum)
