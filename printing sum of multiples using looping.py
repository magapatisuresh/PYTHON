#Printing all multiples 3 or 5:
n=int(input("Enter a nmber:"))
i=1
s=0
while (i < n):
    if i%3==0 or i%5==0:
         s += i
    i += 1
print(s)
