#sort a k sorted array 
#O(n log k)

import heapq as h

def sort_k_sorted_arr(k_arr, k):
    min_heap = []
    sorted_arr = []
    for heap_idx in range(k + 1):
        h.heappush(min_heap, k_arr[heap_idx])

    heap_idx += 1

    while heap_idx < len(k_arr):
        h.heappush(min_heap, k_arr[heap_idx])
        sorted_arr.append(h.heappop(min_heap))
        heap_idx += 1

    while len(min_heap) > 0:
        sorted_arr.append(h.heappop(min_heap))

    return sorted_arr


print sort_k_sorted_arr([1,3,2,5,4,6,4,7,8,6,7], 3)