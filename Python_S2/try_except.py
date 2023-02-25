try:
    a= int(input("Enter a number : "))
    while a>=0:
        if a>=0:
            print("Your number is ",a)
        elif a<=0:
            print("Your number is ",a)
        else:
            print("Enter a integer value only.")
        break
except:
    print("Invalid Syntax!")
finally:
    print("This function is done.")
