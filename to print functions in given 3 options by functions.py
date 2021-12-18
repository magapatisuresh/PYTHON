#1. find if a number is even or odd
#2. print all numbers in a given range
#3. print all the odd numbers in a given numbers
print ("choose any option 1,2,3")
print("1. find if a number is even or odd") 
print("2. print all the numbers in a given range")
print("3.print all the odd numbers in a given range")






opt = int(input())
if opt==1:
    n=int(input("Enter a number"))
    if even_odd(n) :
       print("Even")
    else :
      print("Odd")
elif opt == 2:
    a, b =map(int, input("Enter two numbers").split())
    for i in range (a, b+1):
        if eve_odd(i)==true :
            print(i, end = " ")
else :
    c, d =map (int,input("Enter two numbers").split())
    for i in range (c, d+1):
        if even_odd(i)==fales:
            print(i, end = " ")

