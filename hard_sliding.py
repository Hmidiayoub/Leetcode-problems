from collections import Counter   
def minWindow(s: str, t: str) -> str:
    len1, len2 = len(s), len(t)
    window, count = {}, Counter(t)
    left = 0
    have, need = 0, len2
    res, res_len = [-1,-1], float("inf")
    if len(t) > len(s) :
        return ""
    for right in range(len1) :
        c = s[right]
        window[c] = 1 + window.get(c, 0)
        if c in t and window[c] == count[c] :
            have += 1
        print(window)
        print(f"that's have {have}")
        while have == need :
            if (right - left + 1) < res_len :
                res = [left, right]
                res_len = right - left + 1
            window[s[left]] -= 1
            if s[left] in t and window[s[left]] < count[s[left]] :
                have -= 1
            left += 1
    l, r = res
    print(f"from {l} to {r}") 
    return s[l:r+1]

s = "aaaaaaaabbbbbcdd"
t = "abcdd"
print(minWindow(s, t))