#given a corpus of valid words, design a fucntion that takes a word as in put and
#outputs all valid anagrams of that word

def gen_anagrams(word):
    new_anagram = list(word)
    anagrams = set()
    anagrams.add("".join(new_anagram))
    if len(word) == 2:
        anagram = list(word[1] + word[0])
        anagrams.add("".join(anagram))
        return anagrams

    for idx, letter in enumerate(word):
        temp_anagram = word[:idx] + word[idx + 1:]
        partial_anagrams = gen_anagrams(temp_anagram)

        for partial_anagram in partial_anagrams:
            for new_idx in range(len(word)- 1):

                new_anagram = list(partial_anagram)
                new_anagram.insert(new_idx, letter)
                anagrams.add("".join(new_anagram))

    return anagrams

anagrams = gen_anagrams("gabcdefh")
for anagram in anagrams:
    print anagram
print len(anagrams)