def gen_permutations(input_list):
    if len(input_list) == 2:
        return [input_list, [input_list[1], input_list[0]]]
    
    all_permutations = []
    
    for outer_idx, item in enumerate(input_list):
        prefixes = gen_permutations(input_list[:outer_idx])
        suffixes = gen_permutations(input_list[outer_idx:])
        for prefix in prefixes:
            for suffix in suffixes:
                all_permutations.append(prefix + item + suffix)
                
    return all_permutations

        
    

def permutations_length_n(input_set, n):
    all_subsets = gen_subsets(input_set, n)
    all_susbets_proper_length = set()
    for subset in all_subsets:
        if len(subset) < n: 
            size_diff = n - len(subset)
            new_list = []
            for item in list(subset):
                new_list.extend(size_diff * [item])
            new_subsets = gen_subsets(new_list, size_diff)
            for new_subset in new_subsets:
                if len(new_subset) == size_diff:
                    all_susbets_proper_length.add(tuple(list(subset) + list(new_subset)))
        else:
            all_susbets_proper_length.add(tuple(subset))
            
    return all_susbets_proper_length
             

def gen_subsets(input_list, length):
    all_subsets = set()
    for i in range(2 ** len(input_list)):
        new_subset = []
        for j in range(len(input_list)):
            if i >> j & 1 == 1:
                new_subset.append(input_list[j])
        if len(new_subset) <= length and len(new_subset) > 0:
            all_subsets.add(tuple(new_subset))
            
    return all_subsets
        
        

permutations_length_n([1,2], 3)
print gen_permutations([1,2,3])
#def gen_permutations(input_set, length):
    