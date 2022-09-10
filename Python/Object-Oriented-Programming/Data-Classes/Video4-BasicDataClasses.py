"""
Basic Data Classes

We're going to create a data class that represents a location along
with its latitude and longitude

The Dataclass is created using the @dataclass decorator in the line preceding the class
definition statement. The colon format is used to specify what data type the attribute
will be
"""
from dataclasses import dataclass

@dataclass
class Position:
    name: str # simply list fields wanted in class
    lon: float # the colon is used to specify the data type
    lat: float


pos = Position('Oslo', 10.8, 59.9)
print(pos)
print(pos.lat)
print(f'{pos.name} is at {pos.lat}N, {pos.lon}E')

"""
You can also make dataclasses using a named tuple like format
"""
from dataclasses import make_dataclass
Position = make_dataclass('Position', ['name', 'lat', 'lon'])


"""
Dataclass included methods

Dataclasses behave like a standard class. The difference is that data classes contain
methods for __init__, __repr__, and __eq__ already implemented for you

This makes adding default values very easy.

Type hints are mandatory. You can use any from the typing module as a workaround. however
these types are not enforced. 
"""
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


print(Position('Null Island'))
print(Position(name='Greenwich', lon=0.0, lat=51.8))

"""
Adding methods is similar to that in standard class
"""
from math import asin, cos, radians, sin, sqrt
@dataclass
class Position2:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2 + cos(phi_1) * cos(phi_2) * sin((lam_2 -lam_1)/2)**2)
        return 2 * r * asin(sqrt(h))


oslo = Position2('Oslo', 10.8, 59.9)
vancouver = Position2('Vancouver', -123.1, 49.3)

print(oslo.distance_to(vancouver))


