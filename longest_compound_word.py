#longest compound word that can be made of other compound words in the list
#assuming no overlapping words


def longest_compound(words):
    sorted_words = sorted(words, key=lambda x: len(x))
    print sorted_words

    for long_idx in range(len(sorted_words) - 1, -1, -1):
        cur_word = sorted_words[long_idx]
        for short_idx, word in enumerate(sorted_words[:long_idx]):

            if len(cur_word) > 0:
                cur_word = cur_word.replace(word, "")
            if len(cur_word) == 0:
                return sorted_words[long_idx]

    return False







words = ['cat', 'cats', 'catsdogcats', 'catxdogcatsrat', 'dog', 'dogcatsdog', 'hippopotamuses', 'rat', 'ratcat', 'ratcatdog', 'ratcatdogcat']

print longest_compound(words)