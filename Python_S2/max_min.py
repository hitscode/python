
def max(x,y):
    z=0
    w=list1[0]
    for d in x:
        if d>=z:
            z=d
    for d in y:
        if d<=w:
            w=d
    return z,w

list1=[]
n=int(input("How many:"))
for x in range(n):
    list1.append(int(input("num:")))

print("")
a,b=max(list1,list1)
print("")
print("max",a)
print("min",b)
