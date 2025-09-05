def temparaturesNextMax(temperatures) :
    n = len(temperatures)
    output = []
    right = 1
    left = 0
    while left < n-1 :
        if temperatures[left] < temperatures[right] :
            output.append(right-left)
            left += 1
            right = left + 1
        else :
            if right < n-1 :
                right += 1
            else :
                output.append(0)
                left += 1
                right = left + 1  
    output.append(0)  
    return output
temps = [30,38,30,36,35,40,28]
print(temparaturesNextMax(temps))