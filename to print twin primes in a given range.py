# To print twin prime pairs in a given range
def prime (n):
     if n==1:
          return False
     for i in range (2, n//2+1):
          if n%i==0:
               return False
     return True
a,b = map(int, input().split())
for i in range (a, b+1):
     if prime(i) and prime(i+2):
          print (i, i+2)

