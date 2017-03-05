import pdb
'''Given a list_of_ints, find the highest_product you can get from three of the integers.'''

class MaxHeap(object):
    def __init__(self):
        self.elems = []

    def paren_idx(self, idx):
        return (idx - 1)/2

    def swap(self, idx1, idx2):
        temp = self.elems[idx1]
        self.elems[idx1] = self.elems[idx2]
        self.elems[idx2] = temp

    def insert(self, item):
        if len(self.elems) >= 1:
                self.elems.append(item)
                self.bubble_up(len(self.elems) - 1)
        else:
            self.elems.append(item)

    def left_idx(self, idx):
        return idx * 2 + 1

    def right_idx(self, idx):
        return idx * 2 + 2

    def bubble_up(self, item_idx):
        if item_idx != 0:
            if self.elems[item_idx] > self.elems[self.paren_idx(item_idx)]:
                self.swap(item_idx, self.paren_idx(item_idx))
                self.bubble_up(self.paren_idx(item_idx))

    def pop(self):
        if len(self.elems) > 0:
            ret_val = self.elems[0]
            self.elems[0] = self.elems[-1]
            del self.elems[-1]
            self.bubble_down(0)
            return ret_val

    def bubble_down(self, idx):
        if self.left_idx(idx) < len(self.elems) and self.right_idx(idx) < len(self.elems):
            if self.elems[self.left_idx(idx)] > self.elems[self.right_idx(idx)]:
                self.swap(self.left_idx(idx), idx)
                self.bubble_down(self.left_idx(idx))
            else:
                self.swap(self.right_idx(idx), idx)
                self.bubble_down(self.right_idx(idx))
        elif self.left_idx(idx) < len(self.elems):
            self.swap(self.left_idx(idx), idx)
            self.bubble_down(self.left_idx(idx))



def highest_product_three_elems(arr):
    largest_positives = MaxHeap()
    largest_negatives = MaxHeap()
    zero_count = 0

    for elem in arr:
        if elem > 0:
            largest_positives.insert(elem)
        elif elem < 0:
            largest_negatives.insert(elem)
        else:
            zero_count += 1

    largest_two_negatives = []
    for i in range(2):
        largest_two_negatives.append(largest_negatives.pop())

    largest_three_positives = []
    for i in range(3):
        largest_three_positives.append(largest_positives.pop())

    max_prod = 1
    if len(largest_positives) + len(largest_negatives) < 3:
        max_prod = 0
    elif largest_two_negatives[0] * largest_two_negatives[1] > largest_three_positives[1] * largest_three_positives[2]:
        max_prod *= largest_three_positives[0] * largest_two_negatives[0] * largest_two_negatives[1]
    else:
        max_prod *= largest_three_positives[0] * largest_three_positives[1] * largest_three_positives[2]

    return max_prod

