def PermutedStrings(s,e) :
    size, tize = len(s), len(e)
    if size != tize :
        return False
    hash = {}
    for char in s :
        hash[char] = hash.get(char, 0) + 1 
    for char in e :
        if char not in hash :
            return False
        hash[char] -= 1
        if hash[char] < 0 :
            return False
    return True
s = 'cccccccccccccccccccccbba'
e = 'ccccccccbcccccccccbccac'
print(f' || these 2 strings are {PermutedStrings(s,e)} the same')