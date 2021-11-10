# To print the length of given number:
n=int(input("Enter a number:"))
l=0
while n:
    r = n%10
    l += 1
    n = n//10
print(l)

