n=int(input("Enter your roll no:"))
p=int(input("Enter your physics marks:"))
c=int(input("Enter your chemistry marks"))
s=int(input("Enter your computer science marks:"))
t=(p+c+s)
q=(t/3)
print("Roll no:",n)
print("Total marks:",t)
print("Percentaga:",q)

if q>=80 :
    print("Division:first")
elif q>=70:
    print("Division:second")
elif q>=60:
    print("Division:third")
elif q>=50:
    print("Division:fourth")
else :
    print("Division:fail")

