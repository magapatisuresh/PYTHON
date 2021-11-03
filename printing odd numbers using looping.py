# Print odd numbers by using loop concept

a=int(input())
b=int(input())
while a <= b:
    if a%2 != 0:
        print(a,end = " ")
    a += 1
