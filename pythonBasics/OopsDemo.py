# Classes are  user defined blueprints or prototypes
# sum, add, multiply, divide, constant
# method, instance variables, class variables, constructors
# objects for your classes
# self keyword is mandatory for calling variable names into methods
# instance and class variables have whole different purpose
# constructor name should be def__init__(self):


class Calculator:
    num = 100
# default constructor

    def __init__(self, a, b):
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when object is created")


    def GetData(self):
        print("I am now executing as a method inside a class")
    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num



obj = Calculator(2, 3) # syntax to create objects in python
obj.GetData()   # syntax to call methods of class in python
print(obj.num)  # syntax to call variables of class in python

# for calling class variables either use self.variable name or classname.variable name
# for calling instance variables always use self.variablename

obj1 = Calculator(4, 5)
obj1.GetData()
print(obj1.Summation())






