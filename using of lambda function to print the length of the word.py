# Using lambda function to split a word
# To split a word and find the length of the word

l= list(map(lambda s:[s, len(s)],input().split()))
print (l)
