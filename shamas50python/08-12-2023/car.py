class car:
    def __init__(self,clr,price,km):
        self.clr=clr
        self.price=price
        self.km=km
    def __gt__(self,others):
        if(self.price>others.price):
            return True
        else:
            return False
    def __add__(self,others):
        return self.km+others.km
c1=car("Black",1200,2000)
c2=car("red",1300,2500)
if(c1>c2):
    print("car1 price is high")
else:
    print("car2 price is high")
print(c1+c2)
