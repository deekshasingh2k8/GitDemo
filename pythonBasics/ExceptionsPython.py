ItemsInCart = 0
# 2 items will be added to cart


if ItemsInCart != 2:       # raise Exception("products cart count not matching")

    pass                       # using pass keyword means above line will do nothing

# assert (ItemsInCart == 2)       # assertion error

# assert (ItemsInCart == 0)

# try, catch : used very frequently when we are not sure a popup is there or not in a landing page

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except:
    print("Somehow i reached here due to failure in try block")   #  to know the actual reason of the error in catch block


try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:                       # to know the actual reason of the error in catch block
    print(e)

