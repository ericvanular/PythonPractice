#find all values within some range in an array


def find_nums_within_k_range(arr, k):
    sorted_arr = sorted(arr)
    all_groups = []

    for idx in range(len(sorted_arr)):
        sub_group = []
        if idx != 0:
            if sorted_arr[idx] == sorted_arr[idx - 1]:
                continue
        for sub_group_idx in range(idx, len(sorted_arr)):
            if sorted_arr[sub_group_idx] - sorted_arr[idx] > k:
                break
            else:
                sub_group.append(sorted_arr[sub_group_idx])
        if len(sub_group) > 1:
            all_groups.append(sub_group)

    return all_groups

print find_nums_within_k_range([1,2,2,2,3,3,3,4], 1)