from .output import Output

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

    def process(self, input_):

        matrix = 

        availableRides = set(input_.rides)
        vehiclesRides = {vehicle: [] for vehicle in input_.vehicles}
        vehicleNextAvailable = {vehicle: 0 for vehicle in input_.vehicles}
        time = 0
        while time < input_.steps:
            if len(availableRides) == 0:
                break
            availableVehicles = {vehicle for vehicle, availableTime in vehicleNextAvailable.items() if availableTime <= time}
            for vehicle in availableVehicles:
                ride = self.find_best_ride(currentTime=time, timeLeft=input_.steps-time, vehicle=vehicle, availableRides=availableRides, bonusFactor=input_.bonusFactor)
                # print(vehicle, ride)
                if not ride:
                    continue
                availableRides.remove(ride)
                vehicle.position = ride.endPosition
                vehiclesRides[vehicle].append(ride)
                vehicleNextAvailable[vehicle] = ride.length + max(vehicle.position.distance_to(ride.startPosition), ride.earliestStartTime)
            time += 1
        return Output(vehiclesRides=vehiclesRides)
