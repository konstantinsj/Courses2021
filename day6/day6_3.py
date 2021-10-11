# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in reverse form. - not the whole text reversed!!
#
# Example
# Alus kauss mans -> Sula ssuak snam
# PS Split and join operations could be useful here.

sentence = input("Input the sentence: ")
words = sentence.split()
reversed_words = [word[::-1] for word in words]
reversed_sentence = ' '.join(reversed_words).capitalize()
print(f"{sentence} -> {reversed_sentence}")
