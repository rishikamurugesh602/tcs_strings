string=input()
def remove_brackets(s):
    res=[]
    for ch in s:
        if ch in "()[]{}":
            continue
        res.append(ch)
    return "".join(res)
   
print(remove_brackets(string))
