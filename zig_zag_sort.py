arr = [4,3,7,8,6,2,1,5,6,7,8,3,1,2,6,1,7,9,3,7,2,1]

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

def zig_zag_sort(arr):
    order_less_greater = True
    
    for idx in range(len(arr) - 2):
        if order_less_greater:
            if arr[idx] > arr[idx + 1] > arr[idx + 2]:
                swap(arr, idx + 1, idx + 2)
            elif arr[idx] < arr[idx + 1] < arr[idx + 2]:
                swap(arr, idx, idx + 1)  
        else:
            if arr[idx] > arr[idx + 1] > arr[idx + 2]:
                swap(arr, idx, idx + 1)
            elif arr[idx] < arr[idx + 1] < arr[idx + 2]:
                swap(arr, idx + 1, idx + 2) 
        order_less_greater = not order_less_greater
                
    
print arr
zig_zag_sort(arr)
print arr
            
                