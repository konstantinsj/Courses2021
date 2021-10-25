# 1. The Shuffle
#
# write  a function get_shuffled_cards()
# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]
#
# The function returns a shuffled set of cards - the same list with tuples but shuffled!
# Find the correct method from built in random library.
#
# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html

import itertools
import random


def get_shuffled_cards():
    suit = "diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"
    card = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"
    card_list = list(itertools.product(suit, card))
    random_card = random.choice(card_list)
    print(random_card)


get_shuffled_cards()


# 2. Deck
#
# write a class Deck with the following attributes(variables)
# available - contains list of card tuples that can be used
# spent - contains list of card tuples that have been used
# there should be following methods:

# constructor (__init__) method
# initializes available with full 52 card list of tuples
# initializes spent with empty list

# shuffle(self):
# # shuffles available cards - works just like 1st function but works on available

# get_cards(self, count=1):
# # gets some number(default 1) of cards from available
# adds these cards to spent
# returns these cards
#
# # you can add other methods and/or attributes if you wish to Deck class


class Deck:

    def __init__(self, card_list="", spent=""):
        suit = "diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"
        card = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"
        self.card_list = (list(itertools.product(suit, card)))
        self.spent = ""
        available = set(card_list) - set(spent)
        print(self.card_list)

    def shuffle(self):  #random card
        random_card = random.choice(self.card_list)
        print(random_card)
        return self


new_deck = Deck()
random_card = Deck.shuffle(new_deck)