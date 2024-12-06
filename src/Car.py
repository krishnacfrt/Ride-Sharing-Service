from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self,numberPlate):
        super().__init__(numberPlate)
    
    def get_fare_per_km(self):
        return 20