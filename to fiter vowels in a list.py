# Lambda function to filter vowels in a list
l=list(filter(lambda s:True if s in "aeiou" else False, input()))
print(l)
