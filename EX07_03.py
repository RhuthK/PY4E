fileInput = input('Enter the file name : ')

try:
    file = open(fileInput)
    
except:
    if fileInput == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd! ")
        quit()
    else:
        print("File cannot be opened: ", fileInput)
        quit()


count = 0 
for line in file:
    count += 1

print('There were', count, 'subject lines in', fileInput )
