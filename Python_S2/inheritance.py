class base:
    name= "Hitesh"
    def display(self):
        print("(base)Name: " ,self.name)

class derived(base):
    id=465
    def display(self):
        print("(derived)Name:" , self.name)
    
class superDerivedClass(derived):
    def display(self):
        print("(super)Name:",self.name, "id :" ,self.id)

base_obj=base()
base_obj.display()

der_obj = derived()
der_obj.display()

sd= superDerivedClass()
sd.display()