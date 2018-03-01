from .output import Output
import numpy as np

class Processor:

    def get_score(self, vehicle, ride, steps, bonusFactor):
        if ride.completed:
            return 0
        earliestPossibleStartTime = vehicle.earliest_possible_start_time(ride, steps)
        if earliestPossibleStartTime is None:
            return 0
        waitTime = earliestPossibleStartTime - ride.earliestStartTime
        rideFinishTime = max(earliestPossibleStartTime, ride.earliestStartTime)  + ride.length
        rideCannotFinish = rideFinishTime > ride.latestFinishTime
        if rideCannotFinish:
            return 0
        rideFinishesAfterSteps = rideFinishTime >= steps
        if rideFinishesAfterSteps:
            return 0
        return ride.length + (bonusFactor if waitTime == 0 else 0)

    def process(self, input_):
        steps = input_.steps
        bonusFactor = input_.bonusFactor
        vehicles = np.array(input_.vehicles)
        rides = np.array(input_.rides)
        matrix = np.zeros((len(vehicles), len(rides)))
        for vehicleIndex, vehicle in enumerate(vehicles):
            for rideIndex, ride in enumerate(rides):
                matrix[vehicleIndex][rideIndex] = self.get_score(vehicle=vehicle, ride=ride, steps=steps, bonusFactor=bonusFactor)
        print('running')
        totalScore = 0
        while True:
            # print(matrix)
            # print(matrix)
            vehicleIndex, rideIndex = np.unravel_index(matrix.argmax(), matrix.shape)
            # print(vehicleIndex, rideIndex)
            maxScore = matrix[vehicleIndex][rideIndex]
            if maxScore == 0:
                break
            totalScore += maxScore
            ride = rides[rideIndex]
            vehicle = vehicles[vehicleIndex]
            # print(vehicle, ride)
            ride.completed = True
            vehicle.do_ride(ride, steps)
            matrix[:,rideIndex] = 0
            for rideIndex, ride in enumerate(rides):
                matrix[vehicleIndex][rideIndex] = self.get_score(vehicle=vehicle, ride=ride, steps=steps, bonusFactor=bonusFactor)
        vehiclesRides = {vehicle.vehicleId: [r.ride for r in vehicle.ridesCompleted] for vehicle in vehicles}
        print('unfinished ride count', sum((1 if not r.completed else 0) for r in rides))
        print('score', totalScore)
        return Output(vehiclesRides=vehiclesRides)
