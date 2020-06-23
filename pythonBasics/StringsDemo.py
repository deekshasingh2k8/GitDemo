str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"
print(str[1])        # a
print(str[0: 5])     # Rahul,if you want to print substring in python
print(str + str1)    # concatenate two strings
print(str3 in str)   # substring check

var = str.split(".")
print(var)            # returns the splited values in a list form
print(var[0])         # extract value from a list
str4 = "  Great  "
print(str4.strip())
print(str4.rstrip())
print(str4.lstrip())