"""
Data classes for representation

Recall that we can print a deck

We can create a better more readable representation of the object
    - Dataclasses don't implement __str__ method by default
    - We can define a better method
"""
from PythonDataClasses.Video6_AdvancedDefaultValues import *
print(Deck())

@dataclass
class PlayingCard7:
    rank: str
    suit: str

    def __str__(self):
        return f"{self.suit}{self.rank}"


RANKS7 = "2 3 4 5 6 7 8 9 10 J Q K A".split()
SUITS7 = "\u2660 \u2662 \u2661 \u2663".split()


def make_french_deck7():
    return [PlayingCard7(r, s) for s in SUITS7 for r in RANKS7]


class Deck7:
    cards: List[PlayingCard7] = field(default_factory=make_french_deck7)

    def __repr__(self):
        cards = ", ".join(f"{c!s}" for c in self.cards)
        return f"{self.__class__.__name__}({cards})"


print(Deck7())