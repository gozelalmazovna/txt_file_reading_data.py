#Initialize variables
count = 0
pos = 0
num = 0

#Ask for a file name
fname = input("Enter the name:")

#Check the file name
try:
    fhand = open(fname,"r") #if true open it
except:
    print("Invalid file name") #if false quit
    quit()

#Search for a lines 'X-DSPAM-Confidence:    0.8475'
#Count them and find average of floating numbers

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    pos = line.find("0")
    num = num + float(line[pos:])

#Print the output
print("Average spam confidence:", num/count)
