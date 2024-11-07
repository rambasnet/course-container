"""
Unittesting Triangle class
"""

__author__ = "Ram Basnet"
__date__ = "2024/11/5"
__license__ = "MIT"
__version__ = "2.0.0"
__maintainer__ = "Ram Basnet"


import unittest
from triangle import Triangle


class TestTriangle(unittest.TestCase):
    """
    Unittesting Triangle class
    """

    def setUp(self) -> None:
        """
        Setup method - creates a triangle object every time a test is run
        """
        self.triangle = Triangle(3, 4, 5)

    def test_perimeter(self) -> None:
        """
        Tests perimeter method
        """
        self.assertEqual(self.triangle.perimeter, 12)

    def test_area(self) -> None:
        """Tests area attribute
        """
        self.assertEqual(self.triangle.area, 6)

    def test_sides(self) -> None:
        """
        Tests getSides method
        :return: None
        """
        self.assertEqual(self.triangle.sides, (3, 4, 5))

    def test_is_right_angled(self) -> None:
        """Tests is_right_angled method
        """
        self.assertTrue(self.triangle.is_right_angled())

    def test_is_right_angled2(self) -> None:
        """Tests is_right method
        """
        self.triangle.set_sides(3, 4, 6)
        self.assertFalse(self.triangle.is_right_angled())

    def test_is_right_ngled3(self) -> None:
        """Tests isRight method
        """
        self.triangle.set_sides(3, 4, 7)
        self.assertFalse(self.triangle.is_right_angled())

    def test_str(self) -> None:
        """Tests __str__ method
        """
        self.assertEqual(str(self.triangle),
                         'Triangle: side1 = 3 side2 = 4 side3 = 5')

    def test_repr(self) -> None:
        """Tests __repr__ method
        """
        self.assertEqual(repr(self.triangle),
                         'Triangle: side1 = 3 side2 = 4 side3 = 5')
