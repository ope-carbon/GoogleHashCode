
class Position:

    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column

    def __repr__(self):
        return '{cls}(row={row}, column={column})'.format(cls=self.__class__.__name__, row=self.row, column=self.column)

    def __str__(self):
        return self.__repr__()

    def distance_to(self, otherPosition):
        return abs(self.row - otherPosition.row) + abs(self.column - otherPosition.column)
