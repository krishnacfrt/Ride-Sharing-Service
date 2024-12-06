from abc import ABC, abstractmethod

class FareStrategy(ABC):
    @abstractmethod
    def calc_fare(self, vehicle, distance):
        pass

# standart fare strateggy 
class StandardFareStrategy(FareStrategy):
    def calc_fare(self, vehicle, distance):
        return vehicle.get_fare_per_km() * distance

# shared_fare_strategy.py
class SharedFareStrategy(FareStrategy):
    def calc_fare(self, vehicle, distance):
        return vehicle.get_fare_per_km() * distance * 0.5


# luxury_fare_strategy.py
class LuxuryFareStrategy(FareStrategy):
    def calc_fare(self, vehicle, distance):
        # Additional 50% surcharge for luxury ride
        return vehicle.get_fare_per_km() * distance * 1.5
