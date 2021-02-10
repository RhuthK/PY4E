'''Write a program to read through a mail log, build a
histogram using a dictionary to count how
many messages have come from each email address, and print the dictionary.'''



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
        # print(line)

        if line not in dictionary:
            dictionary[line] = 1
        else:
            dictionary[line] += 1

print(dictionary)
