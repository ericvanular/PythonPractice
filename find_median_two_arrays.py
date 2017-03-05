#find the median of two arrays

arr1 = [5, 2, 3, 4, 6]
arr2 = [0, 1, 5, 1, 2]

def find_median(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    arr_comb = []

    idx_1 = 0
    idx_2 = 0

    total_length = len(arr1) + len(arr2)
    total_idx = 0

    last_queue = [-1,-1]#first_elem, last_elem

    while total_idx < total_length/2:
        if idx_1 == len(arr1):
            idx_2 += 1
            last_queue[-1] = last_queue[0]
            last_queue[0] = 2
        elif idx_2 == len(arr2):
            idx_1 += 1
            last_queue[-1] = last_queue[0]
            last_queue[0] = 1
        elif arr1[idx_1] < arr2[idx_2]:
            idx_1 += 1
            last_queue[-1] = last_queue[0]
            last_queue[0] = 1
        else:
            idx_2 += 1
            last_queue[-1] = last_queue[0]
            last_queue[0] = 2
        total_idx += 1


    print last_queue

    if total_length % 2 != 0:
        if last_queue[0] == 1:
            median = arr1[idx_1]
        else: #if last_queue[0] == 2:
            median = arr2[idx_2]
    else:
        if last_queue[0] == 1:
            median = arr1[idx_1]
        else:# last_queue[0] == 2:
            median = arr1[idx_1]
        if last_queue[1] == 1:
            median += arr1[idx_1 - 1]
        else:# last_queue[1] == 2:
            median += arr2[idx_2 - 1]
        median = float(median) / 2

    return median

    print last_queue
    print "array 1: " + str(arr1) + " idx: " + str(idx_1)
    print "array 2: " + str(arr2) + " idx: " + str(idx_2)
    arr_comb = sorted(arr1 + arr2)
    print arr_comb

print find_median(arr1, arr2)

