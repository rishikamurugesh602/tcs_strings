string=input()
def solution(s):
    ans=""
    res=[]
    hashmap={}
    for ch in s:
        hashmap[ch]=hashmap.get(ch,0)+1
    for ch in s:
        if hashmap[ch]>1:
            ans+=ch
            hashmap[ch]=0
    return ",".join(ans)

print(solution(string))
            
