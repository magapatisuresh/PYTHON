#Printing of numbers and multiples in backward :
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
while b >= a:
    i = 12
    while i  >= 1:
        print(b, 'x', i, '=', b*i)
        i -= 1
    print()
    b -= 1
     
