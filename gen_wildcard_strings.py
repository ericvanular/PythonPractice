#generate all string combos where '?' char is a wildcard (can be 1 or 0)


def string_combos(input_string):
    num_quotes = 0
    broken_input_string = input_string.replace('??', '?!?')
    broken_input_string = broken_input_string.split('?')
    
    #print broken_input_string
    
    for char in input_string:
        if char == '?':
            num_quotes += 1
            
    combos_0_1 = []
    for i in range(2 ** num_quotes):
        bin_val = str(bin(i))[2:]
        bin_prefix = '0' * (num_quotes - len(bin_val) )
        bin_string = bin_prefix + bin_val
        combos_0_1.append(bin_string)
        
    new_strings = set()
        
    for combo in combos_0_1:
        new_string = ""
        for idx, substring in enumerate(broken_input_string[:-1]):
            new_string += substring
            new_string += combo[idx]
        new_string += broken_input_string[-1]
        new_string = new_string.replace('!','')
        new_strings.add(new_string)
        
    return new_strings
            
        
    
print string_combos('0?1????0')