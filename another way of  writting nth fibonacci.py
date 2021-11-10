#Another way to write fibonacci:
n=int(input("Enter a number"))
a = 0
b = 1
while n>0:
    print(a, end = ' ' )
    a, b = b, a+b
    n -= 1
