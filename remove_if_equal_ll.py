#remove all nodes in Linked List if they match a values

class LL:
    def __init__(self, head):
        self.head = head

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

    def set_next(self, next):
        self.next = next


def remove_if_equal(prev_node, curr_node, val):
    has_removed = False
    if curr_node.val == val:
        has_removed = True
        if curr_node.next is not None:
            prev_node.next = curr_node.next
        elif curr_node.next is None:
            prev_node.next = None
    return has_removed

def remove_val_from_ll(ll, val):
    curr_node = ll.head
    if curr_node is not None:
        if curr_node.val == val:
            ll.head = curr_node.next

        prev_node = ll.head
        curr_node = ll.head.next

        while curr_node is not None:
            if remove_if_equal(prev_node, curr_node, val) == False:
                prev_node = curr_node
            curr_node = curr_node.next



def print_ll(ll):
    curr_node = ll.head
    while curr_node is not None:
        print curr_node
        curr_node = curr_node.next

ll_lst = [
Node(5),
Node(4),
Node(4),
Node(2),
Node(5),
Node(5),
Node(1),
Node(8),
Node(5),
]



ll = LL(ll_lst[0])

for idx,elem in enumerate(ll_lst):
    if idx != len(ll_lst) - 1:
        ll_lst[idx].set_next(ll_lst[idx + 1])


print_ll(ll)

remove_val_from_ll(ll, 5)

print "\n"

print_ll(ll)