#Find factors for t times
t=int(input("Enter t"))
for number in range (t):
    n=int(input("Enter a number"))
    s=0
    for i in range (1, n//2+1):
        if n%i==0:
            s+=i
    if s==n:
        print(n,'is perfect')
    else :
        print(n,'is not perfect')
