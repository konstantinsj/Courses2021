# 3. Is there a pangram?
#
# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')
# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise
#
# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram
#
# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a
#
# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False
#
# Bonus: test it also on Latvian alphabet:
# a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
# print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv)) -> True

def is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz'):
    t = text.strip().lower().replace(" ", "").replace(",", "")
    return set(t) >= set(alphabet)

print(is_pangram("The five boxing wizards jump quickly"))
print(is_pangram("Not a pangram"))