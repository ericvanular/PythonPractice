#convert a decimal number to binary, flip its nth bit, convert back to decimal

def dec_to_bin(num):
    bin_val = []
    while num > 0:
        bit = num % 2
        bin_val.insert(0,bit)
        num = num // 2
    return bin_val



def bin_to_dec(num_lst):
    total = 0
    for indx, bit in enumerate(num_lst):
        power = len(num_lst) - indx - 1
        total += (bit * 2**power)
    return total

def flipbit(num, bit):
    bin_num = dec_to_bin(num)
    which_bit = len(bin_num) - bit
    
    if bin_num[which_bit] == 0:
        bin_num[which_bit] = 1
    else:
        bin_num[which_bit] = 0
        
    dec_num = bin_to_dec(bin_num)
    
    return dec_num

print flipbit(100,3)