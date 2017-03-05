#only one element occurs an even number of times, print that element

def even_occuring(arr):
    sorted_arr = sorted(arr)
    num_occurances = 1

    for idx, elem in enumerate(sorted_arr):
        if idx != 0:
            if elem != sorted_arr[idx - 1]:
                if num_occurances % 2 == 0:
                    return sorted_arr[idx - 1]
                num_occurances = 0
            num_occurances += 1

    if num_occurances % 2 == 0:
        return sorted_arr[idx]

    return None

print even_occuring([1,2,3,2,2,3,3,4,1,4,1,4,6,6,0])