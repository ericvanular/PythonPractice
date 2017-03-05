https://www.careercup.com/question?id=16759664
list1 = [4,10,15,24,26]
list2 = [0,9,12,20]
list3 = [5,18,22,30]

l1_idx = 0
l2_idx = 0
l3_idx = 0

min_range = max(list1[l1_idx], list2[l2_idx], list3[l3_idx]) - min(list1[l1_idx], list2[l2_idx], list3[l3_idx])

last_flag = 0

while l1_idx < len(list1) and l2_idx < len(list2) and l3_idx < len(list3):
    
    curr_range = max(list1[l1_idx], list2[l2_idx], list3[l3_idx]) - min(list1[l1_idx], list2[l2_idx], list3[l3_idx])
    
    if curr_range <= min_range:
        min_range = curr_range
    
    if min(list1[l1_idx], list2[l2_idx], list3[l3_idx]) == list1[l1_idx]:
        l1_idx += 1
        last_flag = 0
    elif min(list1[l1_idx], list2[l2_idx], list3[l3_idx]) == list2[l2_idx]:
        l2_idx += 1
        last_flag = 1
    elif min(list1[l1_idx], list2[l2_idx], list3[l3_idx]) == list3[l3_idx]:
        l3_idx += 1
        last_flag = 2
        
      
        

print 'min range: ' + str(min_range)

if last_flag == 0:
    l1_idx -= 1
elif last_flag == 1:
    l2_idx -= 1
elif last_flag == 2:
    l3_idx -= 1

print 'A idx: ' + str(l1_idx) + ' A val: ' + str(list1[l1_idx])
print 'B idx: ' + str(l2_idx) + ' B val: ' + str(list2[l2_idx])
print 'C idx: ' + str(l3_idx) + ' C val: ' + str(list3[l3_idx])