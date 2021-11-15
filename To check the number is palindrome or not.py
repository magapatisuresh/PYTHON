# To check whether the number is a palindrome or not
n=int(input("Enter a number"))
t=n
r=0
while n:
    x = n%10
    r = r*10+x
    n = (n//10)
if r==t:
    print("Palindrome")
else :
    print("Not a palindrome")
    
