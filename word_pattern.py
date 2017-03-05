#check if the relative order of words in a string are the same as a pattern


def word_pattern(pattern, string):
    
    string_to_list = string.split(" ")
    if len(pattern) != len(string_to_list):
        return False
    
    pattern_table = dict()

    for idx, char in enumerate(pattern):
        if not pattern_table.has_key(char):
            pattern_table[char] = idx

    string_table = dict()

    for idx, word in enumerate(string_to_list):
        if not string_table.has_key(word):
                string_table[word] = idx

    for char, word in zip(pattern, string_to_list):
        if string_table[word] != pattern_table[char]:
            return False

    return True


pattern = "abba"
string = "dog cat cat dog"
print word_pattern(pattern, string)