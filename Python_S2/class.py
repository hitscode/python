class student:
    __stdmarks=15
    def display(self):
        print("Marks : ",self.__stdmarks)

stdobj=student()
stdobj.display()
print("Marks : ",stdobj.__stdmarks)