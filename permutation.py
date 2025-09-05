
from collections import Counter
def checkInclusion(s1: str, s2: str) -> bool:
    len1, len2 = len(s1), len(s2)
    if len1 > len2:
        return False

    count1 = Counter(s1)
    count2 = Counter(s2[:len1])

    if count1 == count2:
        return True

    for i in range(len1, len2):
        count2[s2[i]] += 1
        count2[s2[i - len1]] -= 1
        if count2[s2[i - len1]] == 0:
            del count2[s2[i - len1]]
        if count1 == count2:
            return True

    return False

s1 = "abc"
s2 = "cccccbabbbaaaa"
print(checkInclusion(s1, s2))