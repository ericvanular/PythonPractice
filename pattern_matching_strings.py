def letters_ordinal(input_string):
    d = dict()
    for idx, letter in enumerate(input_string):
        if not d.has_key(letter):
            d[letter] = idx
    return d

def pattern_match(pattern_string, test_string):
    if len(pattern_string) != len(test_string):
        return False
    pattern_ordinal = letters_ordinal(pattern_string)
    test_ordinal = letters_ordinal(test_string)
    pattern_arr = []
    for letter in pattern_string:
        letter_ord = pattern_ordinal[letter]
        pattern_arr.append(letter_ord)
        
    for idx, letter in enumerate(test_string):
        letter_ord = test_ordinal[letter]
        if letter_ord != pattern_arr[idx]:
            return False
    return True
        
    
pattern_string = 'accb'
test_string = 'cddf'
print pattern_match(pattern_string, test_string)
