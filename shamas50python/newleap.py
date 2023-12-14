a=int(input("enter current year:"))
b=int(input("enter a final year:"))
    
for i in range(a,b+1):
    if (i%4==0)&(i%100!=0)|(i%400==0):
        print(i)
