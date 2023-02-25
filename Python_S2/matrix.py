m1=[]
m2=[]
c=[]
n=int(input("Enter order of matrix: "))
n*=n
for i in range(n):
    a=int(input("Enter element : "))
    m1.append(a)

for j in range(n):
    b=int(input("Enter element : "))
    m2.append(b)

if n==1:
    print("matrix1 : ")
    print(m1[0])
    print("matrix2 : ")
    print(m2[0])