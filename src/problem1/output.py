

class Output:

    def __init__(self, vehiclesRides):
        self.vehiclesRides = vehiclesRides

    def write_to_file(self, outputFile):
        with open(outputFile, 'w') as solFile:
            for vehicle, rides in sorted(self.vehiclesRides.items()):
                outputText = '{rideCount} {rides}\n'.format(rideCount=len(rides), rides=' '.join([str(ride.rideId) for ride in rides]))
                solFile.write(outputText)
