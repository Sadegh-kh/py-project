from math import hypot
class Point:

    """
    A point on the two-dimensional coordinate axis
    #exampel
    >>> p1 =Point(3,5)
    >>> p2=Point(1,2)
    >>> p2.rest()
    >>> p1.distance(p2)
    5
    methods:
        move:


    #attribute
    #interface
    """

    def __init__(self, x: float, y: float) -> None:
        """
        initialize x y coordinates of new point

        :param x: float x-coordinate
        :param y: float y-coordinate
        """
        self.x = x
        self.y = y

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def rest(self):
        self.move(0, 0)

    def distance(self, other: "Point") -> float:
        return hypot(self.x - other.x, self.y - other.y)

