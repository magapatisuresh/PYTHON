#To find  repettive sum of digits of a given number:
n=int(input("Enter a number:"))
s=0
while True:
    s = 0
    while n:
        r = n%10
        s += r
        n = n//10
    if s<10:
        break
    n = s
print(s)


 
     
    
