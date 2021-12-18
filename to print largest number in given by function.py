# To print the largest number by function
def greater (a, b):
    if a>b :
        print(a, "is grater")
    else :
        print(b, "is greater")
x, y =map(str,input().split())
greater (x, y)
