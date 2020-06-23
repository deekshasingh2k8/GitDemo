file = open('test.txt')
# Read all the contents of the file
# print(file.read(5))   # read n no of characters by passing parametes,line change is also considered one byte.
# print(file.readline())  # read a line of characters
# print(file.readline())  # No of readline methods means no of lines will be readed


# iq: Print line by line using readline method if 100 lines are there
# Method1 : while loop

# line = file.readline()
# while line != "":
#    print(line)
#    line = file.readline()

# method 2: file.readlines: returns the whole content of a file as a list with lines as the indexes
# in the form of values = ["abc", "bvdsf","cat", "dog","elephant]

for line in file.readlines():
    print(line)



file.close()