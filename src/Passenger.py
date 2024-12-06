from User import User

class Passenger(User):
    def __init__(self, name, email, location):
        super().__init__(name, email, location)

    def notify(self, msg):
        print(f"Passenger: {msg}")

