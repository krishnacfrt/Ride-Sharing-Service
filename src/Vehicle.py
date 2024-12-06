from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, number_plate):
        self._number_plate = number_plate

    @abstractmethod
    def get_fare_per_km(self):
        pass
