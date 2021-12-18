# To print the minimum value in list witout using
# min function list element value less than 10000
l=list(map(int,input().split()))
m=10000
for i in l:
   if i<m:
    m = i
print(m)
