a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a>b and a>c:
    print("The biggest number is:",a)
elif a<b and b>c:
    print("The biggest number is:",b)
elif a<c and c>b:
    print("The biggest number is:",c)
elif a==b==c:
    print("The numbers",a,b,c,"Are equal")
