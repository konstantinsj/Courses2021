import itertools
import random


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
        card = "K", "A"
        # suit = "diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"
        # card = 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"
        self.spent = spent
        self.card_list = (list(itertools.product(suit, card)))

    def display_cards(self):
        print(f"Available cards {self.card_list}")

    def shuffle(self):  # shuffle cards
        random.shuffle(self.card_list)
        print(f"Shuffled cards: {self.card_list}")
        return self

    def get_cards(self, count=1):
        if count > len(self.card_list):
            print("Cant get that much!")
        else:
            self.spent = self.card_list[:count]
            del self.card_list[0:count]
            print(f"Got cards: {self.spent}")
            # self.card_list = list(set(self.card_list)-set(self.spent))  set solution, but cards are shuffled
        return self


new_deck = Deck()
new_deck.shuffle()
new_deck.get_cards()
new_deck.display_cards()
