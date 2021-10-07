# 2. Almost Hangman
#
# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
#
# If the letter is found, then the letter is displayed in ALL the appropriate places, all other letters remain
# asterisks.
#
# Example:
#
# First input: Kartupeļu lauks -> ********* *****
#
# Second input: a -> *a****** *a***

word = (input("1st player, whats your word? ").lower())
# word = "kartupelu lauks"

guess_text = ""
for c in word:  # masking chars with *
    if c == " ":
        guess_text += " "
    else:
        guess_text += "*"
print(guess_text)

while word != guess_text:  # asking for input until it matches
    guess = (input("2nd player, guess the letter! ").lower())
    for i, c in enumerate(word):
        if c == guess:
            guess_text = guess_text[:i] + guess + guess_text[i + 1:]
    print(guess_text)

print(f"Congratz, you guessed it! {word}")
