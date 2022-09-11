"""
You can subclass dataclasses quite freely

We'll creat a subclass to contain capitals. Inheritance works smoothly
when there are no default values.

When there are defaults it gets a little more complicated
"""
from dataclasses import dataclass
@dataclass
class Position:
    name: str
    lon: float
    lat: float


@dataclass
class Capital(Position):
    country: str


print(Capital('Oslo', 10.8, 59.9, 'Norway'))


"""
Default value examples

The reason is because we have a variable without a default value(Capital)
after parameters with default arguments (lon and lat)

The fix is to add a dummy default value.

If we change the default for an attribute in the child class the order of
attributes will come from the parent first.
"""
@dataclass
class Position2:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capital2(Position2):
    country: str = 'Unknown'
    lat: float = 40.0 # order of attrs is still name, lon, lat, country


print(Capital2('Oslo', 10.8, 59.9, 'Norway'))
