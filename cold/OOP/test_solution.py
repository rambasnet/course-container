"""Unittesting Solution class."""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


import unittest
from unittest.mock import patch
from io import StringIO
from cold_oop import Solution


class TestSolution(unittest.TestCase):
    """
    Unittesting Solution class
    """

    def setUp(self) -> None:
        """ Setup method - called before each test"""
        self.sol = Solution()
        self.input1 = open('../data/1.in', 'r', encoding='utf-8')
        self.input2 = open('../data/2.in', 'r', encoding='utf-8')

    def tearDown(self) -> None:
        """ Tear down method - called after each test"""
        self.input1.close()
        self.input2.close()
        return super().tearDown()

    def test_read_data1(self) -> None:
        """Tests readData method"""
        self.sol.read_data(self.input1)
        self.assertEqual(self.sol.get_n(), 3)
        self.assertEqual(self.sol.get_data(), '5 -10 15')

    def test_read_data2(self) -> None:
        """
        Tests readData method
        :return: None
        """
        self.sol.read_data(self.input2)
        self.assertEqual(self.sol.get_n(), 5)
        self.assertEqual(self.sol.get_data(), '-14 -5 -39 -5 -7')

    def test_find_answer1(self) -> None:
        """Tests findAnswer method"""
        self.sol.read_data(self.input1)
        expected = self.sol.find_answer()
        self.assertEqual(expected, 1)

    def test_find_answer2(self) -> None:
        """Tests findAnswer method"""
        self.sol.read_data(self.input2)
        expected = self.sol.find_answer()
        self.assertEqual(expected, 5)

    # @patch('sys.stdout', new_callable=StringIO)
    # @patch('sys.stderr', new_callable=StringIO)
    def test_solve1(self) -> None:
        """ Tests solve method - using patch context manager
        - tests 1.in
        """
        # self.sol.solve()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.sol.solve(self.input1)
            self.assertEqual(mock_stdout.getvalue(), '1\n')

    @patch('sys.stdout', new_callable=StringIO)
    def test_solve2(self, mock_stdout: StringIO) -> None:
        """Tests solve method - using patch decorator
        - tests 2.in
        """
        self.sol.solve(self.input2)
        self.assertEqual(mock_stdout.getvalue(), '5\n')
