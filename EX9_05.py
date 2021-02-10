''' This program records the domain name (instead of the address) where the
message was sent from instead of who the mail came from (i.e., the whole email
address).At the end of the program, print out the contents of your dictionary.'''

fileInput = input('Enter a file: ')
try:
    file=open(fileInput)
except :
    print('File cannot be opened')
    exit()

counts = {}
for line in file:
    if line.startswith('From '):
        line = line.rstrip().split()
        line = line[1]
        line = line.split('@')
        line = line[1]
        # print(line)

        if line not in counts:
            counts[line] = 1
        else:
            counts [line] = counts [line] + 1


print(counts)
            
        
        
            

    
            
        
