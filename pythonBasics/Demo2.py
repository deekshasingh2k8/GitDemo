# List
values = [1, 2, "rahul", 4, 5]
# List can have multiple values and in different data-types

print(values[0])  # 1
print(values[3])  # 4
print(values[-1])  # last value-5
print(values[1:3])  # 2 rahul as goes from  0 to -1
values.insert(3, "shetty")
print(values)
values.append("End")
print(values)
values[2] = "RAHUL"  # Updating
del values[0]  # deleting oth index
print(values)

# list is mutable, we can update and change but tuple is not mutable.
# Tuple
# val = (1, 2, "rahul", 4.5)
# print(val[1])

# val[2] = "RAHUL"
# tuple does not support item assignment
# list does this
val = [1, 2, "rahul", 4.5]
print(val[1])

val[2] = "RAHUL"
print(val)

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello World"}
print(dic["a"])
print(dic[4])
print(dic["c"])
print(dic)
# how to build empty dic and add values to dic
dict = {}
dict["firstname"] = "rahul"
dict["lastname"] = "Shetty"
dict["gender"] = "male"

print(dict)
print(dict["lastname"])







