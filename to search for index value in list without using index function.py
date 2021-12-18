# search for items in list as k
#if it found print the index
l=list(map(int,input().split()))
k=int(input())
found = False
for i in range (len(l)):
    if l [i]==k:
        found = True
        break
if found:
    print(k, "found at index",i)
else :
    print("Not found")
