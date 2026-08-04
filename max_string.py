string = input()

def solution(s):
    hashmap = {}

    # Count frequency
    for ch in s:
        hashmap[ch] = hashmap.get(ch, 0) + 1

    # Find maximum frequency
    maxx = max(hashmap.values())

    ans = []

    # Collect all characters having maximum frequency
    for ch in s:
        if hashmap[ch] == maxx and ch not in ans:
            ans.append(ch)

    print("".join(ans))

solution(string)
