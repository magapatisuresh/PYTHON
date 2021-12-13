# Mega prime

#function to find the given number is prime or not
def prime (n):
     if n==1:
          return False
     for i in range (2, n//2+1):
          if n%i==0:
               return False
     return True

# Function to find the all the digits are prime or not

def  digit_prime (x):
     while x:
          r=x%10
          if not prime(r):
               return False
          x=x//10
          return True
     

#function to find if the numbeer is mega prime
def mega_prime(z):
     if prime(z) and digit_prime(z):
          return True
     return False

number = int(input())
if mega_prime(number):
     print("Mega prime")
else :
     print("Not a mega prime")
