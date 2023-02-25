from re import X
num=[]
n=int(input("How many numbers you want to add?? "))
for i in range(0,n):
    n=int(input())
    num.append(n)
print(num)

def sum(a):
    print(a)
    print(type(a))

file_obj=open("myFile.txt",'w')
file_obj.write("hello")
file_obj.write("hey")
file_obj.close()

with open("myFile.txt",'r') as f:
    print(type(f.readline()))
    print(type(f.readlines()))
    print("output from file")
    f.seek(0)#**
    print(f.readline())
    print(f.tell())#**
    f.seek(0)
    print(f.readlines())           