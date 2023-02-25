class Person:
    def __init__(self,name,age,sname):
        self.name=name
        self.age=age
        self.sname=sname
    def myfunc(self):
        print("Hello my name is " + self.name)
p1=Person("Hitesh",19 , "abc")
p1.myfunc()
print(p1.name)
print(p1.age)
print(p1.sname)
p2=Person("Hitman" , 20 , "xyz")