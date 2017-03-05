#given an array representing blocks with width 1, figure our how much water can be stored in the shape

from random import randint

def calc_water(start_idx, end_idx, heights):
    top_level = min(heights[start_idx], heights[end_idx])
    water = 0
    if end_idx - start_idx < 2:
        return 0
    for idx in range(start_idx + 1, end_idx):
        water += top_level - heights[idx]
    return water


heights = [randint(0,10) for i in range(10)]
#heights = [5, 6, 7, 0, 2, 2, 8, 3, 1, 0]
#heights = [1, 1, 4, 0, 3]

max_height = max(heights)
max_height_idxs = []

total_water = 0

for idx, elem in enumerate(heights):
    if elem == max_height:
        max_height_idxs.append(idx)

for idx, elem in enumerate(max_height_idxs):
    if idx != 0:
        total_water += calc_water(max_height_idxs[idx - 1], elem, heights)


start_idx = 0
end_idx = 0

while heights[start_idx] != max_height:
    if heights[end_idx] >= heights[start_idx]:
        total_water += calc_water(start_idx, end_idx, heights)
        start_idx = end_idx
    end_idx += 1


start_idx = len(heights) - 1
end_idx = start_idx
while heights[start_idx] != max_height:
    if heights[end_idx] >= heights[start_idx]:
        total_water += calc_water(end_idx, start_idx, heights)
        start_idx = end_idx
    end_idx -= 1

print heights
print 'total amount of water: ' + str(total_water)


