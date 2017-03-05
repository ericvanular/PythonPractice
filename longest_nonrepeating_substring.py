base_String = 'ABDEFGABEF'


def longest_nonrepeating_substring(base_string):
    last_char_pos = dict()
    longest_substrings = [-1 for i in range(len(base_string))]

    print longest_substrings

    for idx, char in enumerate(base_string):
        if idx == 0:
            longest_substrings[idx] = 1
        else:
            if char not in last_char_pos:
                longest_substrings[idx] = 1 + longest_substrings[idx - 1]
            elif last_char_pos[char] < idx - longest_substrings[last_char_pos[base_string[idx - 1]]]:
                longest_substrings[idx] = 1 + longest_substrings[idx - 1]
            else:
                longest_substrings[idx] = idx - last_char_pos[char]

        last_char_pos[char] = idx

    print longest_substrings

    return max(longest_substrings)



print longest_nonrepeating_substring(base_String)

	