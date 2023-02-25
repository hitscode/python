def fun(*i):
    my_list=list[a]
    mylist=list1[b]
list=[]
list1=[]

operator= input("Enter a operator(+,-,*,/,ev_odd,sqr,sqr_root) :")
if operator== "+":
    num=int(input("How many numbers you want to add? "))
    for b in range (num):
        n=int(input("Enter your number: "))
        list.append(n)
    print(list)
    add=0
    for s in range(len(list)):
        add+=list[s]
    print(add)
elif operator== "*":
    nu=int(input("How many numbers you want to multiply? "))
    for w in range(nu):
        m=int(input("Enter your number: "))
        list1.append(m)
    print(list1)
    multi=1
    for p in range(len(list1)):
        multi= multi*list1[p]
    print(multi)
else:
    num1 = input("Enter your number : ")
    num1 = int(num1)
    if operator== "sqr":
        print("Ans is" ,num1**2 )
    elif operator== "sqr_root":
        print("Ans is" ,num1**0.5)
    elif operator=='ev_odd':
        a=num1%2
        if a==0:
            print("It is an Even value")
        else:
            print("It is an Odd value.")
    else:
        num2 = input("Enter second number : ")
        num2 = int(num2)
        if operator=='-':
            print("Ans is" ,num1-num2)
        elif operator=='*':
            print("Ans is" ,num1*num2)
        elif operator=='/':
            print("Ans is" ,num1/num2)
        else:
                    print("Invalid operator")
print("Thank You")