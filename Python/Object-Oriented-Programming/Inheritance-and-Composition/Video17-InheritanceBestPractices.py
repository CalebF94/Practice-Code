"""
*INHERITANCE BEST PRACTICES*

Follow the Liskov Substitution Principle
    - Manager or Secretary can be substituted where an Employee object is expected
    - Exception types must inherit from BaseException

Think about the 'is a' relationship that inheritance models
    - use inheritance only if the relationship works in one direction
    - see rectangle_square_demo.py
    - We have the case where we changed the size of a square to make it not a s
        square.
"""