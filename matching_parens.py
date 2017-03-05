https://www.interviewcake.com/question/python/matching-parens


word = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

def matching_parens(word, paren_idx):
    curr_paren_ord = 0
    wanted_paren_ord = 0
    
    for idx, char in enumerate(word):
        if char == '(':
            if idx == paren_idx:
                wanted_paren_ord = curr_paren_ord
            curr_paren_ord += 1
            
        elif char == ')':
            curr_paren_ord -= 1
            if curr_paren_ord == wanted_paren_ord:
                return idx
            
            
    return -1



print matching_parens(word, 10)