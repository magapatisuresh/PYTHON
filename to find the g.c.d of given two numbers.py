#To check the G.C.D of given three numbers
a,b = map(int, input().split())
for i in range (b, 0,-1):
    if a%i==0 and b%i==0:
        print (i)
        break
    
