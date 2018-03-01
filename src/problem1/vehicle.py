
class Vehicle:

    def __init__(self, vehicleId, position, currentTime):
        self.vehicleId = vehicleId
        self.position = position
        self.currentTime = currentTime
        self.ridesCompleted = []

    def __eq__(self, other):
        return self.vehicleId == other.vehicleId

    def __hash__(self):
        return hash(self.vehicleId)

    def __repr__(self):
        return '{cls}(vehicleId={vehicleId}, position={position})'.format(cls=self.__class__.__name__, vehicleId=self.vehicleId, position=self.position)

    def __str__(self):
        return self.__repr__()

    def do_ride(self, ride):
        self.currentTime = max(self.currentTime + self.position.distance_to(ride.startPosition), ride.earliestStartTime) + ride.length
        self.position = ride.endPosition
        self.ridesCompleted.append(ride)
