__author__ = 'DpinkyandDbrain'

import Deck


class Dealer:
    def __init__(self):
        self.deck = Deck(False)

    def shuffleDeck(self):
        self.deck = Deck(False)
        self.deck.shuffle()
        self.deck.shuffle()
        self.deck.shuffle()
        self.deck.shuffle()