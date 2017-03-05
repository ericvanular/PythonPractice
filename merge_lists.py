
def merge_lists(lst1, lst2):
    new_list = []
    idx1 = 0
    idx2 = 0
    
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] < lst2[idx2]:
            new_list.append(lst1[idx1])
            idx1 += 1
        else:
            new_list.append(lst2[idx2])
            idx2 += 1
      
    while idx1 < len(lst1):
        new_list.append(lst1[idx1])
        idx1 += 1
    while idx2 < len(lst2):
        new_list.append(lst2[idx2])
        idx2 += 1
        
    return new_list

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)