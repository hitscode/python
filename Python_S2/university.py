class university:
    def __init__(self,year_of_estd,city):
        self.year_of_estd= year_of_estd
        self.city= city
a= input("Designation : ")
if a=="Professor":
    class professor(university):
        def __init__(self, highest_qualification, area_of_research, year_of_joining ,year_of_experience , name_of_institute):
            self.highest_qualification= highest_qualification
            self.area_of_research= area_of_research
            self.year_of_joining=year_of_joining
            self.year_of_experience = year_of_experience
            self.name_of_institute= name_of_institute
        def display(self):
            print("")
            print("Designation : Professor")
            print("Highest Qualification : ", self.highest_qualification)
            print("Research Area : ", self.area_of_research)
            print("Joining Year : ", self.year_of_joining)
            print("Years of Experience : ", self.year_of_experience)
            print("Name of Institute" , self.name_of_institute)
            print("")

elif a=="LA":
    class lab_assistant(university):
        def __init__ (self, highest_qualification, additional_skills , year_of_joining , name_of_institute):
            self.highest_qualification= highest_qualification
            self.additional_skills= additional_skills
            self.yaer_of_joining = year_of_joining
            self.name_of_institute= name_of_institute
        def display(self):
            print("Designation : Lab Assistant")
            print("Highest Qualification : ", self.highest_qualification)
            print("Additional Skills : ", self.additional_skills)
            print("Joining Year : ", self.yaer_of_joining)
            print("Institute Name : ", self.name_of_institute)
            print("")
elif a=="OA":
    class office_assistant(university):
        def __init__(self, highest_qualification, year_of_joining , name_of_institute):
            self.highest_qualification= highest_qualification
            self.year_of_joining= year_of_joining
            self.name_of_institute= name_of_institute
        def display(self):
            print("Designation : Office Assistant")
            print("Highest Qualification : ", self.highest_qualification)
            print("Joining Year : ", self.year_of_joining)
            print("Institute Name : ", self.name_of_institute)
            print("")
elif a=="Peon":
    class peon(university):
            p_qual= input("Enter Your Qualifiacdtion : ")
            p_yoj= int(input("Enter Year Of Joining : "))
            p_ist=input("Enter Institute : ")
            print("")
            print("Designation : Peon")
            print("Qualification : ", p_qual)
            print("Joining Year : ", p_yoj)
            print("Institute Name : ", p_ist)

'''obj_professor= professor("Mtech IT" , "Surat" , 2021 , 4 , "AMTICS")
obj_lab= lab_assistant("Btech CE " , "Communication Skills , Coding" , 2020, "AMTICS")
obj_off= office_assistant("BBA", 2021, "AMTICS")
obj_peon= peon(11, 2020,"AMTICS")

obj_professor.display()
obj_lab.display()
obj_off.display()
obj_peon.display()'''