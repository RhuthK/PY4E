''' Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string,
printing each letter on a seperate line, except backwards. '''


string = input('Insert a word here : ')
length = len(string)-1  
while length:
    print(string[length])
    length -= 1
    if (length == 0):
        print(string[0])
        
        


    
