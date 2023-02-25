class staff:
    def __init__(self, name, age):
        self.name= name
        self.age = age
    
class teacher(staff):
    def __init__(self,department, salary):
        self.department= department
        self.salary = salary
        super().__init__("Hitesh" ,19)
    def display(self):
        print("Name : ", self.name)
        print("Age : ",self.age)
        print("Department : ",self.department)
        print("Salary : ", self.salary)

obj_staff = teacher("AMTICS", 40000)
obj_staff.display()