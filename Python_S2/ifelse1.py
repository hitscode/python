age= input("Enter your age : ")
age=int(age)
if age>= 18 :
    print("You are adult, You can vote.")
elif age<18 and age>3:
    print("You are in school, You can not vote.")
elif age<3 :
    print("You are a child. ")
print("Thank You")