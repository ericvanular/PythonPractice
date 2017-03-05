#https://www.interviewcake.com/question/python/find-rotation-point

words = [
    'retrograde',
    'supplant',
    'undulate',
    'uzl',

    'xenoepist',

    'zen',
    'engender',
    'karpatka',
    'ptolemaic',
]


def is_increasing(words):
    if words[0] < words[1] and words[1] < words[2]:
        return True
    return False

def find_rot(words):

    top = words[0]
    bottom = words[-1]

    if len(words) > 2:

        if is_increasing(words[(len(words)/2) - 1:(len(words)/2) + 2]):
            if top > words[len(words)/2]:
                return find_rot(words[:len(words)/2 + 1])
            else:
                return find_rot(words[len(words)/2:])
        else:
            return min(words[(len(words)/2) - 1:(len(words)/2) + 2])
    else:
        return min(words)

print "answer: " + str(find_rot(words))
