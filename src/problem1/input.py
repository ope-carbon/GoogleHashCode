from problem1.position import Position
from problem1.vehicle import Vehicle
from .ride import Ride
from .grid import Grid


class Input:

    def __init__(self, grid, vehicles, rides, bonusFactor, steps):
        self.grid = grid
        self.vehicles = vehicles
        self.rides = rides
        self.bonusFactor = bonusFactor
        self.steps = steps

    def __repr__(self):
        return '{cls}(grid={grid}, vehicles={vehicles}, rides={rides}, bonusFactor={bonusFactor}, steps={steps})'.format(cls=self.__class__.__name__, grid=self.grid, vehicles=self.vehicles, rides=self.rides, bonusFactor=self.bonusFactor, steps=self.steps)

    def __str__(self):
        return self.__repr__()

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r+') as file:
            content = file.readlines()
        meta = content[0].strip().split()
        bonusFactor = int(meta[4])
        noOfRides = int(meta[3])
        grid = Grid(rows=int(meta[0]), columns=int(meta[1]))
        rawRides = content[1:]
        if len(rawRides) != noOfRides:
            raise Exception('rides missing')
        rides = []
        rideId = 0
        for rawRide in rawRides:
            rawRide = rawRide.strip().split()
            rides.append(Ride(rideId=rideId, startPosition=Position(row=int(rawRide[0]), column=int(rawRide[1])), endPosition=Position(row=int(rawRide[2]), column=int(rawRide[3])), earliestStartTime=int(rawRide[4]), latestFinishTime=int(rawRide[5]), bonusFactor=bonusFactor))
            rideId += 1
        vehicles = []
        for vehicleId in range(int(meta[2])):
            vehicles.append(Vehicle(vehicleId=vehicleId, position=Position(row=0, column=0)))
        return cls(grid=grid, vehicles=vehicles, rides=rides, bonusFactor=bonusFactor, steps=meta[5])
