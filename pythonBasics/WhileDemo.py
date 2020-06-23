it = 10
while it > 1:
    if it == 9:
        it = it-1  # decrement the value of it so stop the infinite loop when it is 9
        continue
    if it == 3:
        break  # break is used to stop the while loop execution
    print(it)  # 10 only as continue statement skips all the below lines of code and go to infinite loop when it = 9.
    it = it-1
print("while loop execution is done")
