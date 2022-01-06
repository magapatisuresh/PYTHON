# To write a program to print how many digits and letters in the given string
s=input()
u=l=d=sp=0
for i in s:
    if 65<=ord(i)<=90 :
        u+=1
    elif 97<=ord(i)<=122:
        l+=1
    elif 48<=ord(i)<=57 :
        d+=1
sp=len(s)-(u+l+d)
print(u,l,d,sp)
        
    
