#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# define a basic function
def funct1():
    print("This is a function.")


# function that takes arguments
def funct2(a, b):
    print(a + b)


# function that returns a value
def funct3(a, b):
    return a ** b


# function with default value for an argument
def funct4(a, b=1):
    return a ** b


# function with variable number of arguments
def funct5(*args):
    add = 0
    for i in args:
        add += i
    print(add)


funct1()
funct2(10, 20)
print(funct3(2, 3))
print(funct4(2))
funct5(10, 20, 30)
