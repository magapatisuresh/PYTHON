# to print multipes of 3 and  5:
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
while a <= b :
    if a%3==0 or  a%5==0:
        print(a,end = " ")
    a += 1
