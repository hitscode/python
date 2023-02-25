class amtics():
    def __init__(self,year,course):
        self.year = year
        self.course= course

class cse(amtics):
    def __init__(self, section, name, entrl_num):
        self.section = section
        self.name = name
        self.entrl_num = entrl_num
        super().__init__(2021, "CSE")
    def display(self):
        print("Year : ", self.year)
        print("Course : ", self.course)
        print("Section : ", self.section)
        print("Name : ", self.name)
        print("Entrollment Num : ", self.entrl_num)

obj = cse("A", "Hitesh" ,465)
obj.display()

print(issubclass(amtics,cse))
print(issubclass(cse,amtics))