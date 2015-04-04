__author__ = 'DpinkyandDbrain'


class Card:
    def __init__(self, suit, value):
        """
        :param suit:
        :param value:
        """
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + ' of ' + self.suit + '\n'
