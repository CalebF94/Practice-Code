"""
Advanced Default Values

AS an example you could have a deck have the default 52 card deck.
    - First specify cards
    - then make function to create deck
"""
from dataclasses import dataclass
from typing import List
@dataclass
class PlayingCard:
    rank: str
    suit: str


# declaring ranks and suits
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS = "\u2660 \u2662 \u2661 \u2663".split()
print(SUITS)


def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]


"""
To use the make_french_deck function for the default value of the Deck class we need
to use the field module. Use default_factory to instantiate with mutable data types. 
The value passed to default_factory needs to be any zero parameter callable

field() Specifier
    - used to customize each field of a data class individually
        - Parameters fields supports
            default: The default value of the field
            default_factory: returns initial value of field
            init: whether field is used in the init method, 
            repr: use the field in repr of object
            compare: use field in comparisons
            hash: include field when calculating hash
            metadata: mapping with info about field
        
"""
from dataclasses import field
@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)


print(Deck())


"""
WE can use the field() method to hide what is shown in the repr or the metadata 
parameter to specify units for lat and lon
A simple example is shown below 
    
    
use can use the fields() method to retrieve the info
"""
@dataclass
class Position:
    name: str
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})

from dataclasses import fields
print(fields(Position))

print(fields(Position)[2].metadata['unit'])