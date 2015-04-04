__author__ = 'DpinkyandDbrain'

import Card
import Hand


class Player:
    def __init__(self, ip, buyIn, chair):
        self.chips = buyIn
        self.ip    = ip
        self.chair = chair

    def recieveHand(self, hand):
        self.hand = hand
