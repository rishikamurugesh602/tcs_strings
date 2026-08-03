string=input()
def first_last(s):
    words=s.split()
    ans=[]
    for word in words:
        if len(word) == 1:
            ans.append(word.upper())
        else:
            ans.append(word[0].upper() + word[1:-1] + word[-1].upper())
    return ' '.join(map(str,ans))
print(first_last(string))
