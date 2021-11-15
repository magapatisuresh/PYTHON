# To reverse the given number:
n=int(input("Enter a number:"))
r=0
while n:
     x = n%10
     r = r*10+x
     n = (n//10)
print(r)
