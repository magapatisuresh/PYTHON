# To find factors by using for loop
n=int(input("Enter a nmber:"))
for i in range(1, n//2+1):
    if n%i==0:
        print(i)
print(n)
