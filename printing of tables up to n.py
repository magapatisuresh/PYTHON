#Printing of numbers upto n:
a=int(input("From"))
b=int(input("To"))
while a <= b:
    i = 1
    print(a, "Table upto??")
    r=int(input())
    while i <= r:
        print(a, "x", i, '=', a*i)
        i +=1
    print()
    a += 1
