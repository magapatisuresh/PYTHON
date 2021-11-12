# To find the given number is near and  power of 2
n=int(input("Enter a number:"))
i=1
while n:
    s = 2**i
    i += 1
    if s>n :
        break
    k = s
print(k)
