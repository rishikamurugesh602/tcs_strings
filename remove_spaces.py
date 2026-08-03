string=input()
def remove_vowels(s):
    res=[]
    for ch in s:
        if ch ==" ":
            continue
        res.append(ch)
    return ''.join(res)
print(remove_vowels(string))
