# Complete the function below.

def is_substring_palindrome(substring):
    char_stack = []
    substring_len = len(substring)
    
    for idx, char in enumerate(substring):
        if idx < substring_len / 2:
            char_stack.append(char)
        if substring_len % 2 == 0:
            if idx >= substring_len / 2:
                if char != char_stack[-1]:
                    return False
                else:
                    char_stack.pop()
        elif substring_len % 2 != 0:
            if idx > substring_len / 2:
                if char != char_stack[-1]:
                    return False
                else:
                    char_stack.pop()
                    
    if len(char_stack) != 0:
        return False
    
    
    return True
                      
def  count_palindromes( S):
    palindromes = []
    substrings = []
    num_palindromes = 0
    for start_idx in range(len(S)):
        for end_idx in range(start_idx, len(S)):
            substring = S[start_idx:end_idx + 1]
            substrings.append(substring)
            is_palindrome = is_substring_palindrome(substring)
            if is_palindrome == True:
                palindromes.append(substring)
                num_palindromes += 1
                
    for s in palindromes:
        print s
    print '\n\n'
    
    for s in substrings:
        print s
    
    return num_palindromes
