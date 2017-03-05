#find all pairs that sum to k

def pairs_sum_to_k(target, arr):
    nums = dict()
    
    pairs = []
    
    for val in arr:
        if nums.has_key(val) == True:
            nums[val] += 1
        else:
            nums[val] = 1

    for num in nums:
        diff = target - num
        if nums.has_key(diff) == True:
            if (nums[diff] > 0 or nums[num] > 0):
                num_occurances_pair = nums[diff] * nums[num]
                for i in range(num_occurances_pair):
                    pairs.append(sorted([num, diff]))
                nums[diff] -= nums[diff]
                nums[num] -= nums[num]                
                
    return pairs


print pairs_sum_to_k(7, [3, 5, 5, 2, 2, 2, -4, 8, 11, 11])
            