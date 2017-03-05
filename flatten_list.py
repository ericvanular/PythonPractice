#flatten a multidimensional array

def flatten(in_arr):
    out_arr = []
    for elem in in_arr:
        if type(elem) != list:
            out_arr.append(elem)
        else:
            sub_arr = flatten(elem)
            out_arr.extend(sub_arr)
        
    return  out_arr

print flatten([1, 2, [3, [4], 5, 6], 7])
            
    