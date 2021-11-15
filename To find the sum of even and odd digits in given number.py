# To find out the sum of even and odd digits in given number
n=int(input("Enter a number:"))
e_d_s = 0
o_d_s =0
while n:
    r = n%10
    if r%2==0:
        e_d_s += r
    else :
        o_d_s += r
    n=n//10
print(e_d_s ,o_d_s)
