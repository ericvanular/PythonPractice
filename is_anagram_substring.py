#does an anagram of the small string appear as a substring in the large string

def is_anagram_substring(small_string, large_string):
    max_matching = len(small_string)
    curr_matching = 0
    small_string_dict = dict()
    letters_count = dict()
    for letter in small_string:
        if small_string_dict.has_key(letter):
            small_string_dict[letter] += 1
            letters_count[letter] += 1
        else:
            small_string_dict[letter] = 1
            letters_count[letter] = 1
        
    
    for idx in range(len(small_string)):
        if small_string_dict.has_key(large_string[idx]):
            if small_string_dict[large_string[idx]] > 0:
                curr_matching +=1
                small_string_dict[large_string[idx]] -= 1
    
    if curr_matching == max_matching:
            return True  
    
    for start_idx in range(1, len(large_string) - len(small_string)):
        end_idx = start_idx + len(small_string) - 1
        if small_string_dict.has_key(large_string[end_idx]):
            if small_string_dict[large_string[end_idx]] > 0:
                curr_matching +=1
                small_string_dict[large_string[end_idx]] -= 1
        if small_string_dict.has_key(large_string[start_idx - 1]):
            if small_string_dict[large_string[start_idx - 1]] < letters_count[large_string[start_idx - 1]]:
                small_string_dict[large_string[start_idx - 1]] += 1
                curr_matching -= 1
                
        if curr_matching == max_matching:
            return True
        
    return False


print is_anagram_substring('xyz', 'afdgzxksldfm')
        
        
            
        
        
        