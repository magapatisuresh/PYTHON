# To find perfect number
n=int(input("Enter a number:"))
s=0
for i in range (1, n//2+1):
    if n%i==0:
         s+=i
if s==n:
    print(n,"Is a perfect number")
else :
    print(n,"Is not a perfect number")
