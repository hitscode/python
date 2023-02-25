f = open("practise1.txt", 'a')
f.write(input("Enter a number: "))
f.close()

f = open("practise1.txt", 'r')
print(f.read())
print(type(f.readlines()))