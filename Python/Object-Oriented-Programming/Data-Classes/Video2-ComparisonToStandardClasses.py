"""
Comparison To Standard Classes

Data Classes:
    - Created using the @dataclass Decorator
    - It comes with basic class capabilities already built in
"""
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str


print("\nDataclass Card")
queen_of_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_hearts.rank)
print(queen_of_hearts.suit)
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))


# making a card using a standard class
# notice that a Queen of hearts doesn't equal a queen of hearts
print("\nRegular Card")


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


queen_of_hearts = RegularCard('Q', 'Hearts')
print(queen_of_hearts == RegularCard('Q', 'Hearts'))


"""
Dataclasses contain method for __repr__ and __eq__

To get this in the regular classe you need to overwrite the 
methods for both __repr__ and __eq__
"""
