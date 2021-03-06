"""
Demonstrate a hashable object with ``__hash__`` and ``__eq__`` methods

A hashable object:
    * can be used as the key in a dictionary (``{key: value}``)
    * can be checked for containment in an iterable (``obj1 in [obj1, obj2]``)
"""


class Person:

    """Person object that can be uniquely identified by SSN"""

    def __init__(self, ssn, name):
        self.ssn = ssn
        self.name = name

    def __hash__(self):
        return hash(self.ssn)

    def __eq__(self, other):
        return self.ssn == other.ssn

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Person({0}, {1})".format(repr(self.ssn), repr(self.name))


mike = Person(6547388493, "Mike")
bill = Person(8737233212, "Bill")
bob = Person(23828283828, "Bob")
rob = Person(23828283828, "Rob")


favorite_colors = {mike: "red", bill: "blue", bob: "green"}
favorite_colors[rob] = "yellow"
assert(favorite_colors[bob] == "yellow")
assert(rob in favorite_colors)
assert(bob in favorite_colors)
del favorite_colors[bob]
assert(rob not in favorite_colors)
