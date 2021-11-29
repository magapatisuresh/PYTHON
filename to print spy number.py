#spy number: A number n is called a spy number if sum of digits of that number
#Is equal to product of digits of that number p
n=int(input("Enter a number:"))
s=0
s1=1
while n  :
    r = n%10
    s += r
    s1 *= r
    n = n//10
if s==s1:
 print(" IT IS A spy number")
else :
 print("It is not a spy number")
    
