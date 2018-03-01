
class Position:

    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column

    def distance_to(self, otherPosition):
        return abs(self.row - otherPosition.row) + abs(self.column - otherPosition.column)