# To check the given number is strong prime or not
def prime (n):
    if n==1:
        return False
    for i in range (2, n//2+1):
        if n%i==0:
            return False
    return True
# To check the strong prime
def strong_prime(n):
    if not prime (n)or n==2:
        return False
    k=n-1
    while prime(k)==False:
        k -= 1
    l=n+1
    while prime(l)==False:
        l+=1
    a=(k+l)/2
    if n>a :
        return True

    else :
        return False

n=int(input())
if strong_prime(n):
    print(n, "Is a strong prime")
else :
    print (n, "Is not a strong prime")


a, b = map (int,input("Enter range:").split())
s=0
print("Strong primes in a given range:")
for i in range(a, b+1):
    if strong_prime(i):
        print(i, end = " ")
        s += 1
print ("\n Number of strong primes in a given range:", s)
