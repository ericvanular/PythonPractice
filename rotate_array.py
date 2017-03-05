#Given an array and an index within that array, rotate the array from that index of rotation
#O(n) time and O(1) Space
#Example :
#Input =&gt; [1,2,3,4,5] , 3
#Output =&gt; [4,5,1,2,3]  

def get_gcd(n1, n2):
    if n1 < n2:
        upper_bound = n1
    else:
        upper_bound = n2

    gcd = 1
    for i in range(2, upper_bound + 1):
        if n1 % i  == 0 and n2 % i == 0:
           gcd = i

    return gcd

def right_rotate(arr, num_places):
    gcd = get_gcd(len(arr), num_places)
    last_block_index = len(arr) - gcd

    for offset in range(gcd):
        temp = arr[offset + last_block_index]
        for block in range(last_block_index, 0, -gcd):
            arr[block + offset] = arr[block + offset - gcd]
        arr[offset] = temp

    return arr

def left_rotate(arr, num_places):
    gcd = get_gcd(len(arr), num_places)
    last_block_index = len(arr) - gcd

    for offset in range(gcd):
        temp = arr[offset]
        for block in range(0, last_block_index, gcd):#(last_block_index, 0, -gcd):
            arr[block + offset] = arr[block + offset + gcd]
        arr[last_block_index + offset] = temp

    return arr

arr = [i for i in range(1,13)]
print arr
print left_rotate(arr, 1)
arr = [i for i in range(1,13)]
print right_rotate(arr, -1)