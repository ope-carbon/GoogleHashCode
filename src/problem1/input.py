

class Input:

    def __init__(self, grid, vehicles, rides, bonusFactor, steps):
        self.grid = grid
        self.vehicles = vehicles
        self.rides = rides
        self.bonusFactor = bonusFactor
        self.steps = steps

    @classmethod
    def from_file(cls):
        pass
