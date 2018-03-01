from .position import Position

class CompletedRide:

    def __init__(self, ride, startTime, endTime):
        self.ride = ride
        self.startTime = startTime
        self.endTime = endTime


class Vehicle:

    def __init__(self, vehicleId):
        self.vehicleId = vehicleId
        self.ridesCompleted = []

    def __eq__(self, other):
        return self.vehicleId == other.vehicleId

    def __hash__(self):
        return hash(self.vehicleId)

    def __repr__(self):
        return '{cls}(vehicleId={vehicleId}, position={position})'.format(cls=self.__class__.__name__, vehicleId=self.vehicleId, position=self.position)

    def __str__(self):
        return self.__repr__()

    def earliest_possible_start_time(self, ride, steps):
        firstRideAfterTime = self.first_ride_after_time(time=ride.latestFinishTime)
        lastRideBeforeTime = self.last_ride_before_time(time=ride.earliestStartTime)
        earliestPossibleStartTime = (lastRideBeforeTime.ride.endPosition.distance_to(ride.startPosition) + lastRideBeforeTime.endTime) if lastRideBeforeTime else Position(0, 0).distance_to(ride.startPosition)
        latestPossibleStartTime = ((firstRideAfterTime.startTime + ride.endPosition.distance_to(firstRideAfterTime.ride.startPosition)) if firstRideAfterTime else steps) - ride.length
        return earliestPossibleStartTime if earliestPossibleStartTime <= latestPossibleStartTime else None

    def do_ride(self, ride, steps):
        earliestPossibleStartTime = self.earliest_possible_start_time(ride, steps)
        startTime = max(earliestPossibleStartTime, ride.earliestStartTime)
        completedRide = CompletedRide(ride=ride, startTime=startTime, endTime=startTime + ride.length)
        firstRideAfterTime = self.first_ride_after_time(time=ride.latestFinishTime)
        index = self.ridesCompleted.index(firstRideAfterTime) if firstRideAfterTime else 0
        self.ridesCompleted.insert(index, completedRide)

    def first_ride_after_time(self, time):
        for completedRide in self.ridesCompleted:
            if completedRide.startTime >= time:
                return completedRide
        return None

    def last_ride_before_time(self, time):
        for completedRide in self.ridesCompleted:
            if completedRide.endTime <= time:
                return completedRide
        return None
