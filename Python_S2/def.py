def sum(a,b):
    add= a+b
    print(add)
s= sum(4,3)

def a(*x):
    print(type(x))
    print(x[0])

x=("a","b",1,2)

def myFun(*x):
    print(x[0] + x[2])

myFun(5,2,3)

def amtics(*a):
    print(a)
a=amtics("a","b",1,2)
