
def int_mult(arr):
    val_before_idx = arr[:]
    val_after_idx = arr[:]
    val_except_idx = arr[:]

    tot_before_index = 1
    for idx in range(len(arr)):
        if idx != 0:
            val_before_idx[idx] = tot_before_index
        else:
            val_before_idx[idx] = 0
        tot_before_index *= arr[idx]

    tot_after_index = 1
    for idx in range(len(arr) - 1, -1, -1):
        if idx != len(arr) - 1:
            val_after_idx[idx] = tot_after_index
        else:
            val_after_idx[idx] = 0
        tot_after_index *= arr[idx]

    for idx in range(len(arr)):
        if idx == 0:
            val_except_idx[idx] = val_after_idx[0]
        elif idx == len(arr) - 1:
            val_except_idx[idx] = val_before_idx[len(arr) - 1]
        else:
            val_except_idx[idx] = val_before_idx[idx] * val_after_idx[idx]

    return val_except_idx


    return new_arr

print int_mult([1, 7, 3, 4])