from Ride import Ride
from Ride import RideStatus

class RideMatchingSystem:
    def __init__(self):
        self.available_drivers = []

    def add_driver(self, driver):
        self.available_drivers.append(driver)

    def request_ride(self, passenger, distance, fare_strategy):
        if not self.available_drivers:
            # Mechanism to notify the passenger
            passenger.notify("No drivers are available")
            return

        # Find the nearest driver available
        nearest_driver = self.find_nearest_driver(passenger.get_location())

        # Mediator
        self.available_drivers.remove(nearest_driver)
        ride = Ride(passenger, nearest_driver, distance, fare_strategy)

        # Calculate fare
        ride.calculate_fare()

        passenger.notify(f"Ride scheduled with fare: Rs {ride.get_fare()}")
        nearest_driver.notify(f"You have a new ride request for: Rs {ride.get_fare()}")

        # Change the status of the ride
        ride.update_status(RideStatus.ONGOING)

        # Change the status of the ride after it is finished
        ride.update_status(RideStatus.COMPLETED)
        self.available_drivers.append(nearest_driver)

    def find_nearest_driver(self, passenger_location):
        assigned_driver = None
        min_dist = float('inf')

        for driver in self.available_drivers:
            distance = driver.get_location().calc_distance(passenger_location)
            if distance < min_dist:
                min_dist = distance
                assigned_driver = driver

        return assigned_driver
