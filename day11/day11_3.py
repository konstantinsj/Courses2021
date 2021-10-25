import deck


def main():
    new_deck = deck.Deck()
    new_deck.shuffle()

    print(new_deck.card_list)
    print(new_deck.get_cards(48))
    print(new_deck.card_list)

    new_deck.shuffle()
    print(new_deck.card_list)


if __name__ == "__main__":
    main()
