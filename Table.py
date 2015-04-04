__author__ = 'DpinkyandDbrain'

from Player import Player


class Table:
    seats = []
    def __init__(self, seats):
        self.numSeats = seats

    def playerSits(self,  player):
        for x in range(0, self.numSeats):
            if self.seats[x] is not None:
                self.seats[x] = player

