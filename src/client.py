from Location import Location
from Car import Car
from Bike import Bike
from Driver import Driver
from Passenger import Passenger
from RideMatchingService import RideMatchingSystem
from FareStrategy import StandardFareStrategy, SharedFareStrategy, LuxuryFareStrategy

def main():
    loc1 = Location(12.9716, 77.5946)  # Bangalore
    loc2 = Location(12.9352, 77.6245)  # Near Bangalore
    loc3 = Location(13.0352, 77.6175)  # Another place near Bangalore

    car = Car("AB123CD")
    bike = Bike("XY987Z")

    driver1 = Driver("Alice", "alice@rideshare.com", loc2, car)
    driver2 = Driver("Bob", "bob@rideshare.com", loc3, bike)

    passenger1 = Passenger("John", "john@rideshare.com", loc1)

    ride_matching_system = RideMatchingSystem()
    ride_matching_system.add_driver(driver1)
    ride_matching_system.add_driver(driver2)

    ride_matching_system.request_ride(passenger1, 10, StandardFareStrategy())

if __name__ == "__main__":
    main()
