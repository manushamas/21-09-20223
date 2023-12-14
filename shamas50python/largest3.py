a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if (a>b)&(a>c):
    print("first number is largest",a)
elif (b>a)&(b>c):
    print("second number is largest",b)
else:
    print("third number is largest",c)
