#intersection of two lists
#sort both lists
#keep a pointer for both lists
#if arr1[i] < arr1[j], increment i
#if arr1[i] > arr2[j], increment j
#if equal, add to intersection list


arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]

def intersection_method2(arr1, arr2):

    inter = set()

    arr1_dict = dict()
    for elem in arr1:
        arr1_dict[elem] = True

    for elem in arr2:
        if elem in arr1_dict:
            inter.add(elem)

    return inter

def intersection_method1(arr1, arr2):
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)

    inter = set()

    j = 0
    i = 0

    while i < len(arr1) and j < len(arr2):
        if sorted_arr1[i] < sorted_arr2[j]:
            i += 1
        elif sorted_arr1[i] > sorted_arr2[j]:
            j += 1
        else: #equal
            inter.add(sorted_arr1[i])
            i += 1
            j += 1

    return inter

print intersection_method1(arr1, arr2)