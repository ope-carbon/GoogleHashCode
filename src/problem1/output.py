

class Output:

    def __init__(self, vehiclesRides):
        self.vehiclesRides = vehiclesRides

    def write_to_file(self, outputFile):
        with open(self.outputFile, 'w') as solFile:
            for vehicle, rides in self.vehiclesRides.items():
                outputText = '{vehicle} {rides}\n'.format(vehicle=vehicle.vehicleId, rides=' '.join([ride.rideId for ride in rides]))
                solFile.write(outputText)
