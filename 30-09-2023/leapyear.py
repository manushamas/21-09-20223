year=int(input("enter a year:"))
if (year%4==0)&(year%100!=0)|(year%400==0):
    print("leap year")
else:
    print("not leap year")
