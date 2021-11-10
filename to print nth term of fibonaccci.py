#Writting nth term of fibonacci:
n= int(input("Enter a number:"))
a=0
b=1
while n>1:
    a,b = b, a+b
    n -= 1
print(a)
