problem_input = [['cat', 'cut', True], # true
['cat', 'cats', True], # true
['cat', 'at', True ], #true
['cat', 'act', False], #false
['cat', 'cat', False],] #false


def is_one_edit_apart(str1, str2):
    if len(str1) - len(str2) > 1:
        return False
    
    is_one_edit = False
    
    if len(str1) != len(str2):
        if len(str1) > len(str2):
            longer_string = str1
            shorter_string = str2
        elif len(str1) < len(str2):
            shorter_string = str1
            longer_string = str2
            
        shorter_string_ptr = 0
        longer_string_ptr = 0
        print "longer string " + str(longer_string)
        print "shorter_string " + str(shorter_string)
        
        while shorter_string_ptr < len(shorter_string) \
            and longer_string_ptr < len(longer_string):
            if shorter_string[shorter_string_ptr] != longer_string[longer_string_ptr]:
                if is_one_edit:
                    return False
                longer_string_ptr += 1
                is_one_edit = True
            shorter_string_ptr += 1
            longer_string_ptr += 1
            
        if shorter_string_ptr == longer_string_ptr:
            return not is_one_edit
            
    elif len(str1) == len(str2):
        str1_ptr = 0
        str2_ptr = 0
        while str1_ptr < len(str1) and str2_ptr < len(str2):
            if str1[str1_ptr] != str2[str2_ptr]:
                if is_one_edit:
                    return False
                is_one_edit = True
            str1_ptr += 1
            str2_ptr += 1
            
    return is_one_edit
              
    
for test_case in problem_input:
    result = is_one_edit_apart(test_case[0], test_case[1])
    print "input case: " + str(test_case)
    print "result: " + str(result)
    print "expected: " + str(test_case[2])
    print "\n"
    

        
                
            
    