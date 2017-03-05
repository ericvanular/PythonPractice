#You have two arrays with numbers in them. You have to stop the program once 
#you've found the largest difference between one number in the 1st array and one number in the 
#2nd array. You do not have to return the numbers, just stop once you've found it.  


def find_largest_diff(arr1, arr2):
    min_arr1 = min(arr1)
    min_arr2 = min(arr2)
    max_arr1 = max(arr1)
    max_arr2 = max(arr2)

    if abs(max_arr2 - min_arr1) > abs(max_arr1 - min_arr2):
        return abs(max_arr2 - min_arr1)

    return abs(max_arr1 - min_arr2)

arr1 = [-1,2,-3,4,-5]
arr2 = [-6,7,-8,9,-10]

print find_largest_diff(arr1, arr2)