
greeting = "Good Morning"
a = 4
if a > 2:
# if greeting == "Good Morning":
    print("condition matches")
else:
    print("condition donot match")
print("if else condition code is completed ")

# for loop
obj = 2, 3, 5, 7, 9
for i in obj:
    print(i*2)
# sum of first 5 natural numbers 1+2+3+4+5= 15
summation = 0
for j in range(1, 6):
# range(i,j)-> i to j-1
    summation = summation + j
print(summation)
print("***********************************************************")

for k in range(1, 10, 5):
# 3rd argument means plus5
    print(k)

print("***********skipping 1st index**********************")
for m in range(10):
# if you donot give 1st argument, it will take it as 0
    print(m)


