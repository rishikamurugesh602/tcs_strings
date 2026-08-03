string=input()
def remove_vowels(s):
    vowels=set('aeiouAEIOU')
    result=[]
    for ch in s:
        if ch not in vowels:
            result.append(ch)
    return ''.join(result)
print(remove_vowels(string))
