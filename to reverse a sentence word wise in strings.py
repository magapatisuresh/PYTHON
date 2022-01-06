# To revers a words in a given sentence
s=input()
l=s.split()
for i in range (len(l)):
    l[i] =l[i][::-1]
print(' '.join(l))
