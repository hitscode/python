def common (a,b):
    result =[i for i in a if i in b]
    return result

a=list(input("Enter list1 : "))
b=list(input("Enter list2 : "))
print("Common element are : ")
print(common(a,b))