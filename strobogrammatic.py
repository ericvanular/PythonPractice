#number flipped 180 degrees is the same?

def is_flipped_equiv(num1, num2):
    if num1 == '6' and num2 == '9':
        return True
    elif num1 == '9' and num2 == '6':
        return True
    elif num1 == '8' and num2 == '8':
        return True
    elif num1 == '0' and num2 == '0':
        return True
    elif num1 == '1' and num2 == '1':
        return True
    return False


def strobogrammatic(number):
    
    if len(number) % 2 != 0:
        middle_num = number[len(number)/2]
        if is_flipped_equiv(middle_num, middle_num) is False:
            return False
    
    leading_idx = 0
    trailing_idx = len(number) - 1
    
    for i in range(len(number)/2):
        num1 = number[i]
        num2 = number[len(number) - i - 1]
        if is_flipped_equiv(num1, num2) is False:
            return False
        
        
    return True
        
    
    
print strobogrammatic('68189')