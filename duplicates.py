s = 'deeedbbcccbdaa'
raw_string = s
index_left = 0
index_right = 1
while index_right < len(raw_string):
    if raw_string[index_left] == raw_string[index_right] :
        index_right += 1
    if index_right == len(raw_string) :
        break
    if (raw_string[index_left] == raw_string[index_right]) and (index_right - index_left == 2) :
        raw_string = raw_string[:index_left] + raw_string[index_right+1:]
        index_left = 0
        index_right = 1
        print(raw_string)
    else :
        index_left += 1 
        index_right = index_left + 1
print(raw_string)
            
            
            