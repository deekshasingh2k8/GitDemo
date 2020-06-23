# To open and close a file in two lines

file = open('test.txt')

file.close()

# with open('test.txt', 'r') as file:  # to open the file in readable format
# with open('test.txt', 'w') as file:  # to open the file in editable format

# Req: Read the file and store all the lines in list
# reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()             # ["abc", "bvdsf","cat", "dog","elephant"]
    reversed(content)                        # ["elephant" , "dog", "cat", "bvdsf", "abc",]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


