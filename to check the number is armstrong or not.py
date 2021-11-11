#To check the number is Armstrong number:
n=int(input("Enter a number:"))
t=n
q=n
#Find the length:
l = 0
while n:
    l += 1
    n = n//10
print("length =",l)
# Find the sum of digits powered to l :
s=0
while t:
    r = t%10
    s += r**l
    t = t//10
if s == q:
    print("It is a armstrong number")
else :
    print("It is not an armstrong number")

