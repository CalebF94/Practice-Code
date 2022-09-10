"""
Alternatives to DataClasses

For simple data structures a tuple or dictionary could be used
    - There are some problems
    - need to remember orders
    - need to remember datatypes
    - need to stay consistent with names
    - both don't have attribute names

NamedTuple
    - from collections import namedtuple
    - This recreates the behaviors we had with data class

Why dataclasses instead of NamedTuple
    - Many more features still not shown for Dataclasses
    - There are some undesirable features of Namedtuples
        - Can compare a Namedtuple to regular tuple
        - Hard to change names
        - Tuples are immutable (sometimes good sometimes not)

attrs
    - Dataclasses was inspired by attrs
    - Behaves in a similar manner to Dataclasses
    - Supports converters and validators
    - Not part of Standard Library
    
"""
queen_of_hearts_tuple = ('Q', 'Hearts')
queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}


# Named Tuples
from collections import namedtuple
NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
queen_of_hearts = NamedTupleCard('Q', 'Hearts')
print(queen_of_hearts)
print(queen_of_hearts == NamedTupleCard('Q', 'Hearts'))


# attrs
import attr
@attr.s
class AttrsCard:
    rank = attr.ib()
    suit = attr.ib()


queen_of_hearts = AttrsCard('Q', 'Hearts')
