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
        rideCannotFinish = (ride.earliestStartTime + waitTime + ride.length) > ride.latestFinishTime
        if rideCannotFinish:
            return 0
        return ride.length + (bonusFactor if waitTime == 0 else 0)

    def update_matrix(self, matrix, vehicles, rides):
        pass

    def process(self, input_):
        while True:
            vehicles = np.array(input_.vehicles)
            rides = np.array(input_.rides)
            matrix = np.zeros((len(vehicles), len(rides)))
            print(matrix)
            self.update_matrix(matrix, vehicles, rides)
            print(matrix)
            vehicleIndex, rideIndex = np.unravel_index(matrix.argmax(), matrix.shape)
            ride = rides[rideIndex]
            vehicle = vehicle[vehicleIndex]
            ride.completed = True
            vehicle.currentTime =
            print(vehicleIndex, rideIndex)



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
