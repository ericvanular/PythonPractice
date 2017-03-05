https://www.interviewcake.com/question/python/recursive-string-permutations21


def swap_letters(input_string, idx1, idx2):
    lst = list(input_string)
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp
    return ''.join(lst)
  
    
def concat_prefixes_suffixes(char, prefixes, suffixes):
    permutations = set()
    if len(prefixes) == 0:
        for suffix in suffixes:
            new_permutation = char + suffix
            permutations.add(new_permutation)
    elif len(suffixes) == 0:
        for prefix in prefixes:
            new_permutation = prefix + char
            permutations.add(new_permutation)
    else:
        for prefix in prefixes:
                for suffix in suffixes:
                    new_permutation = prefix + char + suffix
                    permutations.add(new_permutation)
    return permutations

def gen_permutations(input_string):
    permutations = set()
    if len(input_string) == 1:
        permutations.add(input_string)
        return permutations
    if len(input_string) == 2:
        permutations.add(input_string)
        permutations.add(input_string[1] + input_string[0])
        return permutations

    for orig_idx, char in enumerate(input_string):
        for curr_idx in range(len(input_string)):
            
            string_cpy = input_string[:]
            string_cpy = swap_letters(string_cpy, orig_idx, curr_idx)
            prefixes = gen_permutations(string_cpy[:curr_idx]) 
            suffixes = gen_permutations(string_cpy[curr_idx + 1:])
            new_permutations = concat_prefixes_suffixes(string_cpy[curr_idx], prefixes, suffixes)
            permutations = permutations.union(new_permutations)

    return permutations


print gen_permutations('abcdefg')