#check if a linked list is a palindrome


class node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LL:
    def __init__(self, head):
        self.head = head
    def add(self, node):
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node

def is_palindrome(linked_list):
    #find length of ll
    cur_node = linked_list.head
    ll_len = 1
    while cur_node.next is not None:
        cur_node = cur_node.next
        ll_len += 1

    mid_node_idx = ll_len // 2
    cur_node_idx = 0
    stack = []
    cur_node = linked_list.head

    while cur_node_idx < mid_node_idx:
        stack.append(cur_node.val)
        cur_node_idx += 1
        cur_node = cur_node.next


    while cur_node_idx < ll_len:
        if ll_len % 2 != 0 and mid_node_idx == cur_node_idx:
            pass
        else:
            if len(stack) > 0:
                if stack.pop(-1) != cur_node.val:
                    return False
            else:
                return False
        cur_node = cur_node.next
        cur_node_idx += 1

    if len(stack) != 0:
        return False

    return True

my_head = node(0)
my_ll = LL(my_head)
my_ll.add(node(2))
my_ll.add(node(1))
my_ll.add(node(0))

print is_palindrome(my_ll)
