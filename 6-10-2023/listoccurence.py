firstname=['shamas','binshad','rishan','farooq','shafeen','ansar']
count=0
a=str(input("enter the letter to searchlist:"))
for i in firstname:
    for f in i:
        if(f == "a"):
            count=count+1
print("count of",a,"in",firstname,"is",count)
