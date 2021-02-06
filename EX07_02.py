fileInput = input("Enter file name : ")

try :
    file = open(fileInput)
except :
    print("File cannot be opened.")

count = 0
total = 0 
for line in file: 
    line = line.rstrip()
    
    if "X-DSPAM-Confidence: " in line:
        num = line[20:]
        total += float(num)
        count += 1
        # print(num)
    
    else:
        continue

# print(total)
print("Average spam confidence: ", total/count)
