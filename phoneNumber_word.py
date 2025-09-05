def isWordValid(word, programResult) :
    word_pointer = 0
    exist = [False] * len(word)
    for i in range(len(word)) :
        while word_pointer < len(programResult) :
            if word[i] in programResult[word_pointer] :
                exist[i] = True
                word_pointer += 1
                break
            else :
                word_pointer += 1
    if all(exist) :
        result = True
    else : 
        result = False
    return result

def PhoneNumberToWord(phone_number, listOfWords) :
    phoneString = str(phone_number)
    digits = len(phoneString)
    index = 0 
    finalListOfWords = []
    result = [''] * digits
    nums = {
        '2' : 'abc', 
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl', 
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv', 
        '9' : 'wxyz'    
    }
    while index < digits :
        coll = nums[phoneString[index]]
        result[index] += ''.join(coll) 
        index += 1
    print(f"Permutation : {result}")
    for i in range(len(listOfWords)) :
        validity_check = isWordValid(listOfWords[i], result) 
        if validity_check == True :
            finalListOfWords.append(listOfWords[i])
    return finalListOfWords
phone_number = 366227734
listOfWords = ["bb", "bar", "car", "cap", "baz", "foobar", "emo", "cat", "foo"]
print(f"Final valid words : {PhoneNumberToWord(phone_number, listOfWords)}")