# Print fibonacci sequence upto n (Given numbers):
n=int(input("Enter a number"))
a=0
b=1
print(a,b, end = ' ')
c=a+b
while (c <= n):
    print(c,end = ' ')
    a, b = b, c
    c = a + b
