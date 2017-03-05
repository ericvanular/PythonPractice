#min heap implementation

def left(idx):
    left_idx = 2 * idx + 1
    return left_idx

def right(idx):
    right_idx = 2 * idx + 2
    return right_idx

def parent(idx):
    return (idx - 1) // 2

class min_heap:
    def __init__(self):
        self.data = []
        self.size = 0
    def add(self, node):
        self.data.append(node)
        node_idx = self.size
        while node_idx > 0:
            if self.data[parent(node_idx)] > self.data[node_idx]:
                self.swap(node_idx, parent(node_idx))
                node_idx = parent(node_idx)
            else:
                break

        self.size += 1
    def delete(self):
        top = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        self.size -= 1
        node_idx = 0
        while node_idx < self.size:
            if left(node_idx) < self.size and right(node_idx) < self.size:
                if self.data[node_idx] > min(self.data[right(node_idx)], self.data[left(node_idx)]):
                    if self.data[left(node_idx)] < self.data[right(node_idx)]:
                        self.swap(left(node_idx), node_idx)
                        node_idx = left(node_idx)
                    else:
                        self.swap(right(node_idx), node_idx)
                        node_idx = right(node_idx)
                else:
                    break
            elif left(node_idx) < self.size:
                if self.data[node_idx] > self.data[left(node_idx)]:
                    self.swap(left(node_idx), node_idx)
                    node_idx = left(node_idx)
                else:
                    break
            else:
                break




    def swap(self, idx1, idx2):
        temp = self.data[idx1]
        self.data[idx1] = self.data[idx2]
        self.data[idx2] = temp

mh = min_heap()
mh.add(1)
mh.add(3)
mh.add(2)
mh.add(0)
mh.add(4)
mh.add(0)
mh.add(2)
print mh.data
for i in range(2):
    mh.delete()
    print mh.data