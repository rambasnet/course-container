"""
Triangle class
"""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "2.0.0"
__maintainer__ = "Ram Basnet"


from typing import Tuple


class Triangle(object):
    """
    Triangle class
    """

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """
        Constructor
        """
        self._side1: float = side1
        self._side2: float = side2
        self._side3: float = side3

    def set_sides(self, side1: float, side2: float, side3: float) -> None:
        """Sets the sides of the triangle

        Args:
            side1 (float): first side of the triangle
            side2 (float): second side of the triangle
            side3 (float): third side of the triangle
        """
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3

    @property
    def sides(self) -> Tuple[float, float, float]:
        """Returns the sides of the triangle

        Returns:
            Tuple[float, float, float]: sides of the triangle
        """
        return (self._side1, self._side2, self._side3)

    @property
    def perimeter(self) -> float:
        """Finds the perimeter of the triangle

        Returns:
            float: perimeter of the triangle
        """
        return self._side1 + self._side2 + self._side3

    @property
    def area(self) -> float:
        """Finds and returns the area of the triangle using Heron's formula

        Returns:
            float: area of the triangle
        """
        s: float = self.perimeter / 2
        ans: float = (s * (s - self._side1) * (s - self._side2)
                      * (s - self._side3)) ** 0.5
        return ans

    def __str__(self) -> str:
        """Returns the string representation of the object

        Returns:
            str: string representation
        """
        return 'Triangle: side1 = ' + \
            str(self._side1) + ' side2 = ' + \
            str(self._side2) + ' side3 = ' + str(self._side3)

    def __repr__(self) -> str:
        """Returns the string representation of the object

        Returns:
            str: string representation
        """
        return self.__str__()

    def is_right_angled(self) -> bool:
        """Checks if the triangle is right-angled

        Returns:
            bool: True if the triangle is right-angled, False otherwise
        """
        sides = [self._side1, self._side2, self._side3]
        sides.sort()
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
