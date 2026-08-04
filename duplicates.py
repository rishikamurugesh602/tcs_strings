string=input()
def solution(s):
    ans=""
    hashmap={}
    for ch in s:
        if ch not in hashmap:
            hashmap[ch]=1
            ans+=ch
    return ans

print(solution(string))
            
