# 1. What's the frequency?
#
# Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single
# letter applications.
#
# get_char_count ("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, '': 1} # dictionary sequence doesn't matter and
# the whole alphabet doesn't have to be included There may also be a solution with Counter from standard Python
# library but this is definitely not necessary, although it is very elegant smile

def get_char_count(text):
    count = {}
    for n in text:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    return count


print(get_char_count("hubba bubba"))
