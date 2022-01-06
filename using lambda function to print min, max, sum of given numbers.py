# Using lambda function to find max, min, sum of given numbers
# To split a word and find the length of the word

l= list(map(int,input().split()))
print ((lambda x:[min(x), max(x), sum(x), len(x)])(l))
