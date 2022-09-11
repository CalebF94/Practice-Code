"""
We'll look at slots to optimize our classes

__slots__:
    - slots lists variables in a class
    - variables not listed may not be defined
    - defaults aren't allowed
    - this makes them more memory efficient and faster
"""
from dataclasses import dataclass
@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float