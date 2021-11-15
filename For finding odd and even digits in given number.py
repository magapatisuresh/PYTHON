# For finding the odd and even digits in a given number
n=int(input("Enter a number:"))
e_d_c = 0
o_d_c =0
while n:
    r = n%10
    if r%2==0:
        e_d_c += 1
    else :
        o_d_c += 1
    n=n//10
print(e_d_c ,o_d_c)
