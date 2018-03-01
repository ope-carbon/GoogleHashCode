
class Ride:

    def __init__(self, startPosition, endPosition, earliestStartTime, latestFinishTime, bonusFactor):
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.earliestStartTime = earliestStartTime
        self.latestFinishTime = latestFinishTime
        self.bonusFactor = bonusFactor

    @property
    def potentialBonus(self):
        return self.bonusFactor * self.length

    @property
    def length(self):
        return abs(self.startPosition.row - self.endPosition.row) + abs(self.startPosition.column - self.endPosition.column)