string = input()

def anagram(s):
    words = s.split()

    if len(words) != 2:
        return False

    word1 = words[0]
    word2 = words[1]

    if len(word1) != len(word2):
        return False

    freq1 = {}
    freq2 = {}

    for ch in word1:
        freq1[ch] = freq1.get(ch, 0) + 1

    for ch in word2:
        freq2[ch] = freq2.get(ch, 0) + 1

    return freq1 == freq2

print(anagram(string))
