'''Add code to the above program to figure out who
has the most messages in the file. After all the data has been
read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who h
as the most messages and print how many messages the person has. '''

fileInput = input('Enter file name : ')
try:
    file = open(fileInput)
except:
    print('File cannot be opened')
    quit()


dictionary = {}
for line in file:
    if line.startswith('From '):
        line = line.rstrip().split()
        line = line[1]

        if line not in dictionary:
            dictionary[line] = 1
        else:
            dictionary[line] += 1

        

bigcount = 0
bigword = 0
for line,dictionary in dictionary.items():
    if bigcount is None or dictionary > bigcount:
        bigcount = dictionary
        bigword = line
print(bigword,bigcount)
