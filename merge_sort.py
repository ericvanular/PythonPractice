#merge sort


def merge_sort(arr):
    if len(arr)  <= 1:
        return
    mid = len(arr) // 2

    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    temp_arr = []
    i = 0
    j = 0
    k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            k+= 1
            i += 1
        else:
            arr[k] = right_half[j]
            k += 1
            j += 1
    while i < len(left_half):
        arr[k] = left_half[i]
        k+= 1
        i += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        k += 1
        j += 1


alist = [54,26,93,17,77,31,44,55,20]

print alist

merge_sort(alist)

print alist