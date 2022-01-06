# To print vowels in alist
def vowel(s):
    vowels='aeiou'
    if s in vowels:
        return True
    else :
        return False

l=list(filter(vowels, "aeiou"))
print(l)
