string=input()
def count(s):
    vowel=0
    consonant=0
    space=0
    for i in range(len(s)):
        if s[i] in "aeiouAEIOU":
            vowel+=1
        elif s[i]==" ":
            space+=1
        elif s[i].isalpha():
            consonant+=1
    return vowel,space,consonant
print(count(string))
