__author__ = 'DpinkyandDbrain'

import Card
from random import randint


class Deck:

    suits = ['SP', 'DI', 'HE', 'CL']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []

    def __init__(self, usePrint):
        self.usePrint = usePrint
        for c in range(0, 52):
            if self.usePrint:
                print 'Using ' + str(c % 4) + ' with ' + str(c % 13)
            self.suit = self.suits[c % 4]
            self.deck.append(Card(self.suit, self.values[c % 13]))

    def shuffle(self):
        numcards = randint(0, 51)
        if self.usePrint:
            print "Number of cards to shuffle " + str(numcards)
        for i in range(0, numcards - 1):
            choice1 = randint(0, 51)
            choice2 = randint(0, 51)
            if choice1 != choice2:
                if self.usePrint:
                    print 'Switching card ' + str(choice1) + ' with card ' + str(choice2)
                self.deck[choice1], self.deck[choice2] = self.deck[choice2], self.deck[choice1]

    def __str__(self):
        printer = ''
        for card in self.deck:
            printer += str(card)
        return printer