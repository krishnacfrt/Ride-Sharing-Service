from Vehicle import Vehicle
class Bike(Vehicle):
    def __init__(self, numberPlate):
        super().__init__(numberPlate)
    
    def get_fare_per_km(self):
        return 10