def isMatch(s, p) :
    point_S= len(s) - len(p)
    p_num = 0
    newP = []
    if s == p :
        return True
    for i in range(len(p)) :
        point_P = 0
        if p[i] == '*' :
            print(f"point_P{point_P}, point_S {point_S}")
            if point_S < 0 :
                point_S += 2
                newP.pop()
                point_P = point_S + 1
            while point_P <= point_S :
                newP.append(p[i-1])
                point_P += 1 
                print(f"point_P{point_P}, point_S {point_S}") 
        else :
            newP.append(p[i])
    P = ''.join(newP)
    print(f"P = {P}")
    result = []
    while p_num < len(s) :
        if P[p_num] == s[p_num] or P[p_num] == '.' :
            result.append(s[p_num])
            p_num += 1
        else :
            return False
        print(f"result = {result}")
    if result :
        return True
s = 'aaa'
p = 'ab*a*c*a'
print(f"Matching result : {s} =? {{{isMatch(s,p)}}}")