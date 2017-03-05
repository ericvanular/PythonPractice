#sort a string by the order its characters appear in another string

def char_order(sorting_string):
    order = dict()
    count = 0
    for char in sorting_string:
        if not order.has_key(char):
            order[char] = count
            count += 1
    return order


def sort_string(to_sort, sorting_string):
    order = char_order(sorting_string)

    sorted_string_list = [[] for i in range(len(order))]

    for char in to_sort:
        sorted_string_list[order[char]].append(char)

    return sorted_string_list

print sort_string("cabdbdcadcbda", "abcd")