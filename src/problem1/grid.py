
class Grid:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

    def __repr__(self):
        return '{cls}(rows={rows}, columns={cols})'.format(cls=self.__class__.__name__, rows=self.rows, cols=self.columns)

    def __str__(self):
        return self.__repr__()
