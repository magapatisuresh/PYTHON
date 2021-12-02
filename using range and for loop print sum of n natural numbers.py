# Using for loop and range()
#find the sum of first n natural numbers
n=int(input("Enter a number:"))
s=0
for i in range (1,n+1):
    s += i
print(s,end = '')
