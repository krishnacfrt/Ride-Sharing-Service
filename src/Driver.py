from User import User

class Driver(User):
    def __init__(self, name, email, location, vehicle):
        super().__init__(name, email, location)
        self._vehicle = vehicle

    def get_vehicle(self):
        return self._vehicle

    def notify(self, msg):
        print(f"Driver: {msg}")


