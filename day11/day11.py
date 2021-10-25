# 1. The Shuffle
#
# write  a function get_shuffled_cards() Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"),
# ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]
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
    random.shuffle(card_list)
    return card_list