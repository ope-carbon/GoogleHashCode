from .output import Output
import numpy as np

class Processor:

    def get_score(self, vehicle, ride, steps, bonusFactor):
        if ride.completed:
            return 0
        startTimeFromNow = ride.earliestStartTime - vehicle.currentTime
        waitTime = max(vehicle.position.distance_to(ride.startPosition) - startTimeFromNow, 0)
        rideFinishTime = ride.earliestStartTime + waitTime + ride.length
        rideCannotFinish = rideFinishTime > ride.latestFinishTime
        if rideCannotFinish:
            return 0
        rideFinishesAfterSteps = rideFinishTime >= steps
        if rideFinishesAfterSteps:
            return 0
        return ride.length + (bonusFactor if waitTime == 0 else 0)

    def update_matrix(self, matrix, vehicles, rides, steps, bonusFactor):
        for vehicleIndex, vehicle in enumerate(vehicles):
            for rideIndex, ride in enumerate(rides):
                matrix[vehicleIndex][rideIndex] = self.get_score(vehicle=vehicle, ride=ride, steps=steps, bonusFactor=bonusFactor)


    def process(self, input_):
        vehicles = np.array(input_.vehicles)
        rides = np.array(input_.rides)
        matrix = np.zeros((len(vehicles), len(rides)))
        while True:
            # print(matrix)
            self.update_matrix(matrix, vehicles, rides, input_.steps, input_.bonusFactor)
            # print(matrix)
            vehicleIndex, rideIndex = np.unravel_index(matrix.argmax(), matrix.shape)
            # print(vehicleIndex, rideIndex)
            maxScore = matrix[vehicleIndex][rideIndex]
            if maxScore == 0:
                break
            ride = rides[rideIndex]
            vehicle = vehicles[vehicleIndex]
            # print(vehicle, ride)
            ride.completed = True
            vehicle.do_ride(ride)
        vehiclesRides = {vehicle.vehicleId: vehicle.ridesCompleted for vehicle in vehicles}
        return Output(vehiclesRides=vehiclesRides)
