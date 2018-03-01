from .output import Output

class Processor:

    def find_best_ride(self, vehicle, availableRides):
        if len(availableRides) == 0:
            return None
        return list(availableRides)[0]

    def process(self, input_):
        availableRides = set(input_.rides)
        vehiclesRides = {vehicle: [] for vehicle in input_.vehicles}
        vehicleNextAvailable = {vehicle: 0 for vehicle in input_.vehicles}
        time = 0
        while time < input_.steps:
            availableVehicles = {vehicle for vehicle, availableTime in vehicleNextAvailable.items() if availableTime <= time}
            for vehicle in availableVehicles:
                ride = self.find_best_ride(vehicle=vehicle, availableRides=availableRides)
                if not ride:
                    continue
                availableRides.remove(ride)
                vehiclesRides[vehicle].append(ride)
                vehicleNextAvailable[vehicle] = ride.length + max(vehicle.position.distance_to(ride.startPosition), ride.earliestStartTime)
            time += 1
        return Output(vehiclesRides=vehiclesRides)
