string=input()
def count_freq(s):
    count={}
    ans=[]
    for ch in s:
        count[ch]=count.get(ch,0)+1
   
    for ch in sorted(count):
        ans.append(f"{ch}{count[ch]}")
    return ' '.join(map(str,ans))
        
print(count_freq(string))
