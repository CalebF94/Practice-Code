"""
Immutable Dataclasses

For many dataclass immutability is desired.

Simply set frozen=True in the class definition

Be aware that if the dataclass contains mutable fields those
might still change
"""

from dataclasses import dataclass


# making an immutable dataclass
@ dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0
    lat: float = 0

# will throw error
pos = Position('Oslo', 10.8, 59.9)
#pos.name = 'Stockholm'


"""
In the example below both card and deck are immutable,
but the list containing the cards is mutable, so you can
change the cards in the deck
"""
from typing import List
@dataclass(frozen=True)
class ImmutableCard:
    rank: str
    suit: str


@dataclass(frozen=True)
class ImmutableDeck:
    cards: List[ImmutableCard]


q_hearts = ImmutableCard('Q', 'H')
A_s = ImmutableCard("A", "S")

deck = ImmutableDeck([q_hearts, A_s])
print(deck)

# notice that we can change cards
deck.cards[0] = ImmutableCard('7', "D")
print(deck)