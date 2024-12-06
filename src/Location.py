import math

class Location:
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude

    def get_latitude(self):
        return self._latitude

    def get_longitude(self):
        return self._longitude

    def calc_distance(self, other):
        # Euclidean Distance
        dx = self.get_latitude() - other.get_latitude()
        dy = self.get_longitude() - other.get_longitude()
        return math.sqrt(dx * dx + dy * dy)
