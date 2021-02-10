'''Exercise 2: Write a program that categorizes each mail message by
which day of the week the commit was done. To do this look for lines
that start with “From”, then look for the third word and keep a running
count of each of the days of the week. At the end of the
program print out the contents of your dictionary (order does not matter).'''

fileInput = input('Enter a file name : ')

try:
    file = open(fileInput)

except:
    print('File cannot be opened ')
    quit()

counts = dict()

for line in file:
    if line.startswith('From '):
        line = line.rstrip().split()
        line = line[2].rstrip()
        # print(line)

        if line not in counts:
            counts[line] = 1
        else:
            counts[line] += 1


print(counts)
        

        
        



        


       
        







            
        
