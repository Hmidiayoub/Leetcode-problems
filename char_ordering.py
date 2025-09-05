def charachter_ordering(input, order) :
    result = []
    index = 0
    while index < len(order) :
        for i in range(len(input)) :
            if input[i] == order[index] :
                result.append(input[i])
        index += 1
    return ''.join(result)
input = 'caabab'
order = 'bac'
print(charachter_ordering(input,order))