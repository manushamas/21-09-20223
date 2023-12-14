n=int(input("enter the number of list:"))
c="over"
b=[]
for i in range(0,n):
    element=int(input("enter the elements of list:"))
    if element<100:
        b.append(element)
    else:
        b.append(c)
print(b)
