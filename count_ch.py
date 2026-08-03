string1 = input()
string2 = input()

def count_sub(string1, string2):
    count = {}
    count2 = {}
    ans = 0

    for ch in string1:
        count[ch] = count.get(ch, 0) + 1

    for ch in string2:
        count2[ch] = count2.get(ch, 0) + 1

    for ch in count:
        if ch in count2:
            ans += 1

    return ans

print(count_sub(string1, string2))
