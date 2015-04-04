from Table import Table


class Room:
    tables = []

    def __init__(self, tablenum):
        if tablenum == 0:
            tablenum = 8
        for x in range(0, tablenum):
            print 'starting up Table ', x + 1
            self.tables.append(Table(8))
