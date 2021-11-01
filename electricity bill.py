u=int(input("Units consumed:"))
i=int(input("Customer id:"))
s=0.0
if u<=199 :
    b= u * 1.20
elif u>199 and u<400 :
    b= u* 1.50
elif u>=400 and u<600:
    b= u* 1.80
else :
    b= u* 2.00

if b>400:
    s=0.15* b
t=b+s
print(i)
print(u)
print(b)
print(s)
print(t)
    
