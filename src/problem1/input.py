from problem1.position import Position
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
        meta = content[0]
        noOfRides = meta[3]
        grid = Grid(rows=meta[0], columns=meta[1])
        rawRides = content[1:]
        if len(rawRides) == len(noOfRides):
            raise Exception('rides missing')
        rides = [Ride(startPosition=Position(row=rawRide[0], column=rawRide[1]), endPosition=Position(row=rawRide[2], column=rawRide[3]), earliestStartTime=rawRide[4], latestFinishTime=rawRide[5], bonusFactor=rawRide[0]) for rawRide in rawRides]
        return cls(grid=grid, vehicles=meta[2], rides=rides, bonusFactor=meta[4], steps=meta[5])
