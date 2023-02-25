class dunder_demo:
    def __init__ (self,name,id):
        self.name=name
        self.id= id
    def display(self):
        print("Name : ",self.name)
        print("ID : ",self.id)

dunder_obj= dunder_demo("Hit", 465)
dunder_obj.display()