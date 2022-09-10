"""
More Flexible Data Classes

Parameters

field function
"""

from dataclasses import dataclass
from typing import List
@dataclass
class PlayingCard:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: List[PlayingCard]


# We can create a deck with as few as two cards
queen_of_hearts = PlayingCard('Q', 'Hearts')
ace_of_spades = PlayingCard('A', 'Spades')
two_cards = Deck([queen_of_hearts, ace_of_spades])
print(two_cards)