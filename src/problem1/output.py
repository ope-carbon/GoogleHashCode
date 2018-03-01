

class Output:

    def __init__(self, carsWithRides, outputFile):
        self.carsWithRides = carsWithRides
        self.outputFile = outputFile

    def write_to_file(self):
        with open(self.outputFile, 'w') as solFile:
            for carWithRides in self.carsWithRides:
                outputText = '{car} {rides}\n'.format(car=carWithRides[0], rides=' '.join([str(rides) for rides in carWithRides[1]]))
                solFile.write(outputText)
