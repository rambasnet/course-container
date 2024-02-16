__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

"""
Unittesting Temperature class
"""

import unittest
from temperature import Temperature


class TestTemperature(unittest.TestCase):
    """
    Unittesting Temperature class
    """

    def setUp(self) -> None:
        """
        Setup method
        :return: None
        """
        self.temp = Temperature(32)

    def test_set_temp(self) -> None:
        """
        Tests setTemp method
        """
        self.temp.temp = 0
        self.assertEqual(self.temp.temp, 0)

    def test_get_temp(self) -> None:
        """
        Tests getTemp method
        """
        self.assertEqual(self.temp.temp, 32)

    def test_set_unit(self) -> None:
        """
        Tests setUnit method
        """
        self.temp.unit = 'C'
        self.assertEqual(self.temp.unit, 'C')

    def test_get_unit(self) -> None:
        """
        Tests getUnit method
        """
        self.assertEqual(self.temp.unit, 'F')

    def test_is_negative(self) -> None:
        """
        Tests isNegative method
        """
        self.assertFalse(self.temp.is_negative())

    def test_str(self) -> None:
        """
        Tests str method
        """
        self.assertEqual(str(self.temp), '32 F')

    def test_repr(self) -> None:
        """
        Tests repr method
        """
        self.assertEqual(repr(self.temp), '32 F')

    def test_lt(self) -> None:
        """
        Tests lt method
        """
        self.assertFalse(self.temp < Temperature(0))

    def test_gt(self) -> None:
        """
        Tests gt method
        :return: None
        """
        self.assertTrue(self.temp > Temperature(0))

    def test_eq(self) -> None:
        """
        Tests eq method
        :return: None
        """
        self.assertFalse(self.temp == Temperature(0))

    def test_eq_not_implemented(self) -> None:
        """
        Tests __eq__ method not implemented exeception
        """
        self.assertRaises(NotImplementedError, self.temp.__eq__, 0)

    def test_le(self) -> None:
        """
        Tests le method
        :return: None
        """
        self.assertFalse(self.temp <= Temperature(0))

    def test_ge(self) -> None:
        """
        Tests ge method
        :return: None
        """
        self.assertTrue(self.temp >= Temperature(0))

    def tearDown(self) -> None:
        """
        Tear down method
        :return: None
        """
        super().tearDown()
