answer = input('Enter a number : ')
listt = []
try:
    while str(answer) is not 'done':
        listt.append(float(answer))
        answer = input('Enter a number : ')
    
    
except:
    if str(answer) == 'done':
        print('Maximum: ', max(listt))
        print('Minimum: ', min(listt))
    # print(listt)
    else: 
        print('Not a number. Program ended')
        quit()




