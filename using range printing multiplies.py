# Using range
# Print all multiplies of n upto k
n,k=map(int,input().split())
for i in range (n,k+1,n):
    print(i, end = ' ')
