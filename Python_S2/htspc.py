class emp:
    def __init__(self,name,sname,age):
        self.empname= name
        self.empsname= sname
        self.empage = age
    def intro(self):
        print("This is " + self.empname + " here how may i help you sir/ma'am")

emp1=emp("hitesh" , "kumawat" , 19)
emp1.intro()
print(emp1.empname)
print(emp1.empsname)
print(emp1.empage)
print("_________________________________________________________________________________________________")
# from here saff code is continue....

class hts():
    def __init__(self , name , age , course ):
        self.name = name 
        self.age = age
        self.course = course 
 
class staff(hts):
    def __init__(self, member , department , salary ):
        self.member=member
        self. department= department 
        self.salary= salary
        super().__init__(" Hitesh", 20 , "CSE")

    def call(self):
        print('Name :', self.name)
        print('age :' , self.age)
        print ('course :' , self.course)
        print("1:member :" , self.member )
        print('deparetment :' , self.department)
        print('salary :' , self.salary)

stf1=staff('Vishvajit' , 'AMTICS' , 500000 )
stf1.call()
print("______________________________________________________________________________________________")
#inharitance from here ....
class base():
    name="hitesh"
    def callbase(self):
        print("base name is :" , self.name)

class derived(base):
    enrollno=202103103510465
    def callderived(self):
        print("derived class id is :" , self.enrollno)
        
class superderived(derived):
    def callsuper(self):
        print("(super)name :" ,self.name , "\n(super)enrollno :" , self.enrollno)

s1=base()
s1.callbase()

s2=derived()
s2.callderived()

s3=superderived()
s3.callsuper()