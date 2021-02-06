''' demo.txt  -
There once was a ship that put to sea
And the name of that ship was the Billy o' Tea
The winds blew hard, her bow dipped down
Blow, me bully boys, blow (huh) ''' 

# opening the content of the file 
somefile = open('demo.txt')
for lines in somefile:
    print(lines)
print()
print()


# count lines in a file
somefile_1 = open('demo.txt')
count = 0
for line in somefile_1:
    count += 1
print('line count : ' , count )
print()
print()


# Reading the whole file
wholefile = open("demo.txt")
inpt = wholefile.read()
print(len(inpt))
print(inpt[:21])
print()
print()

#Searching through a file
search = open("demo.txt")
for line in search:
    if line.startswith('Blow'):
        print(line)
