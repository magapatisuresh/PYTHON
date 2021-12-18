# to print the maximum value withou using max function

m=0
l=list(map(int,input().split()))
for i in l:
   if i>m:
    m = i
print(m)
