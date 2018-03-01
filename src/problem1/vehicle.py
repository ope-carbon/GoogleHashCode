
class Vehicle:

    def __init__(self, vehicleId, position):
        self.vehicleId = vehicleId
        self.position = position

    def __eq__(self, other):
        return self.vehicleId == other.vehicleId

    def __repr__(self):
        return '{cls}(vehicleId={vehicleId}, position={position})'.format(cls=self.__class__.__name__, vehicleId=self.vehicleId, position=self.position)

    def __str__(self):
        return self.__repr__()
