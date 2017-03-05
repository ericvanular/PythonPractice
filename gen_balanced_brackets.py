#generate all pairs of balanced brackets for a given number of brackets

def gen_balanced_brackets(num_brackets):
    
    #print "num brackets: " + str(num_brackets)
    
    if num_brackets == 1:
        bracket_patterns = set()
        bracket_patterns.add('()')
        return bracket_patterns    
    
    prev_patterns = gen_balanced_brackets(num_brackets - 1)
    
    new_patterns = set()
    
    for pattern in prev_patterns:
        #print "num brackets: " + str(num_brackets)
        #print "num patterns prev: " + str(len(prev_patterns))
        for i in range(num_brackets):
            new_pattern = pattern[:i]
            new_pattern += '()'
            new_pattern += pattern[i:]
            #print new_pattern
            new_patterns.add(new_pattern)
            
    return new_patterns
            
    
    
patterns = gen_balanced_brackets(10)
for pattern in patterns:
    print pattern
    
print "number of combos: " + str(len(patterns))