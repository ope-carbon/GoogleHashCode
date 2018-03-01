from .output import Output
import numpy as np

class Processor:

    def find_best_ride(self, currentTime, timeLeft, vehicle, availableRides, bonusFactor):
        bestRide = None
        highestPoints = 0
        for ride in availableRides:
            startTimeFromNow = ride.earliestStartTime - currentTime
            waitTime = vehicle.position.distance_to(ride.startPosition) - startTimeFromNow
            if waitTime + ride.length >= ride.latestFinishTime:
                # print(vehicle, 'cant finish', ride)
                continue
            points = ride.length + (bonusFactor if waitTime == 0 else 0)
            if points > highestPoints:
                highestPoints = points
                bestRide = ride
        return bestRide

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
            print(matrix)
            self.update_matrix(matrix, vehicles, rides, input_.steps, input_.bonusFactor)
            print(matrix)
            vehicleIndex, rideIndex = np.unravel_index(matrix.argmax(), matrix.shape)
            print(vehicleIndex, rideIndex)
            maxScore = matrix[vehicleIndex][rideIndex]
            if maxScore == 0:
                break
            ride = rides[rideIndex]
            vehicle = vehicles[vehicleIndex]
            print(vehicle, ride)
            ride.completed = True
            vehicle.do_ride(ride)
        for vehicle in vehicles:
            print(vehicle, ridesCompleted)


        # availableRides = set(input_.rides)
        # vehicleNextAvailable = {vehicle: 0 for vehicle in input_.vehicles}
        # time = 0
        # while time < input_.steps:
        #     if len(availableRides) == 0:
        #         break
        #     availableVehicles = {vehicle for vehicle, availableTime in vehicleNextAvailable.items() if availableTime <= time}
        #     for vehicle in availableVehicles:
        #         ride = self.find_best_ride(currentTime=time, timeLeft=input_.steps-time, vehicle=vehicle, availableRides=availableRides, bonusFactor=input_.bonusFactor)
        #         # print(vehicle, ride)
        #         if not ride:
        #             continue
        #         availableRides.remove(ride)
        #         vehicle.position = ride.endPosition
        #         vehiclesRides[vehicle].append(ride)
        #         vehicleNextAvailable[vehicle] = ride.length + max(vehicle.position.distance_to(ride.startPosition), ride.earliestStartTime)
        #     time += 1
        return Output(vehiclesRides={})
