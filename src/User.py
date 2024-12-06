from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, email, location):
        self._name = name
        self._email = email
        self._location = location

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    @abstractmethod
    def notify(self, msg):
        pass
