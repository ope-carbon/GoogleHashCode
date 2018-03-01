
class Ride:

    def __init__(self, rideId, startPosition, endPosition, earliestStartTime, latestFinishTime, bonusFactor):
        self.rideId = rideId
        self.startPosition = startPosition
        self.endPosition = endPosition
        self.earliestStartTime = earliestStartTime
        self.latestFinishTime = latestFinishTime
        self.bonusFactor = bonusFactor

    def __eq__(self, other):
        return self.rideId == other.rideId

    def __repr__(self):
        return '{cls}(rideId={rideId}, startPosition={startPosition}, endPosition={endPosition}, earliestStartTime={earliestStartTime}, latestFinishTime={latestFinishTime}, bonusFactor={bonusFactor})'.format(cls=self.__class__.__name__, rideId=self.rideId, startPosition=self.startPosition, endPosition=self.endPosition, earliestStartTime=self.earliestStartTime, latestFinishTime=self.latestFinishTime, bonusFactor=self.bonusFactor)

    def __str__(self):
        return self.__repr__()

    @property
    def potentialBonus(self):
        return self.bonusFactor * self.length

    @property
    def length(self):
        return self.startPosition.distance_to(otherPosition=self.endPosition)
