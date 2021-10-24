# 2. Common Elements
#
# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
# get_common_elements (seq1, seq2, seq3)
#
# Example:
# get_common_elements ("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element
# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)
#
# 2. b For those with some experience
# BONUS:  make a function that can handle an arbitrary number of input sequences

def get_common_elements(seq1, seq2, seq3):
    result = tuple(set(seq1).intersection(set(seq2)).intersection(set(seq3)))
    print(type(result))
    return result


print(get_common_elements("abc", ['a', 'b'], ('b', 'c')))
