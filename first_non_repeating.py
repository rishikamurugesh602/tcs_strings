string=input()
def non_repeating(s):
    count={}
    res=[]
    for ch in s:
        count[ch]=count.get(ch,0)+1
    for ch in s:
        if count[ch]==1:
            res.append(ch)
    return ','.join(res)
            
print(non_repeating(string))
