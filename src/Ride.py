from enum import Enum

class RideStatus(Enum):
    SCHEDULED = 1
    ONGOING = 2
    COMPLETED = 3


from Passenger import Passenger
from Driver import Driver
from FareStrategy import FareStrategy

class Ride:
    def __init__(self, passenger, driver, distance, fare_strategy):
        self.passenger = passenger
        self.driver = driver
        self.distance = distance
        self.fare_strategy = fare_strategy
        self.fare = 0.0
        self.status = RideStatus.SCHEDULED

    def calculate_fare(self):
        self.fare = self.fare_strategy.calc_fare(self.driver.get_vehicle(), self.distance)

    def update_status(self, status):
        self.status = status
        self.notify_users(status)

    def notify_users(self, status):
        self.passenger.notify(f"Your ride is {status.name}")
        self.driver.notify(f"Ride Status: {status.name}")

    def get_fare(self):
        return self.fare
