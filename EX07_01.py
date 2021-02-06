fileInput = input('Enter a file name : ')

try:
    file = open(fileInput)
   
except:
    print('Your file cannot be opened')
    quit()

for lines in file:
    print(lines.rstrip().upper())
    
    
