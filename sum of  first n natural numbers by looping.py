# Sum of first n natural numbers by using looping:
n = int(input("Enter a number"))
i = int (input("enter a number"))
s = 0
while (i <= n):
    print(s, '+', i, '=', s+i)
    s += i
    i += 1
print("sum is:", s )
    
