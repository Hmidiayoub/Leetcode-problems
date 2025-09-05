def string_words(string, words):
    words_num = 0
    pointer = 0
    is_it_valid = 0
    for word in words :
        for chara in range(len(string)) :
            if word[pointer] == string[chara] :
                words_num += 1
                pointer += 1
            if pointer >= len(word) :
                break
        print(f"word number = {words_num} , length of word {len(word)}")
        if words_num == len(word) :
            is_it_valid += 1
        pointer = 0
        words_num = 0
    return is_it_valid
string = "abcdercb"
words = ["aerc", "bb", "aca", "bde"]
print(string_words(string, words))