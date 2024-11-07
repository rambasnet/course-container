"""
Unittesting Solution class
"""

__author__ = "Ram Basnet"
__date__ = "2024/11/5"
__license__ = "MIT"
__version__ = "2.0.0"
__maintainer__ = "Ram Basnet"


from os import path
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from egypt_abc import Solution


class TestSolution(unittest.TestCase):
    """Unittesting Solution class
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_solve1(self, mock_stdout: StringIO) -> None:
        """Tests solve method
        """
        # source = '6 8 10\n25 52 60\n5 12 13\n0 0 0\n'
        dir_path = path.join(path.dirname(__file__), '../data')
        input_file = path.join(dir_path, '1.in')
        with open(input_file, 'r', encoding='utf-8') as source:
            sol = Solution(source)
            sol.solve()
            sol.print_answer()
            output_file = path.join(dir_path, '1.ans')
            with open(output_file, 'r', encoding='utf-8') as expected:
                self.assertEqual(mock_stdout.getvalue(), expected.read())

    @patch('sys.stdout', new_callable=StringIO)
    def test_solve2(self, mock_stdout: StringIO) -> None:
        """
        Tests solve method
        """
        data2 = '6 8 10\n25 52 60\n5 12 13\n0 0 0\n'
        with patch('sys.stdin', StringIO(data2)):
            sol = Solution(sys.stdin)
            sol.solve()
            sol.print_answer()
            expected: str = 'right\nwrong\nright\n'
            self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_solve3(self, mock_stdout: StringIO) -> None:
        """
        Tests solve method
        """
        data3 = '2 3 4\n20 50 62\n3 4 7\n3 4 5\n0 0 0\n'
        with patch('sys.stdin', StringIO(data3)):
            sol = Solution(sys.stdin)
            sol.solve()
            sol.print_answer()
            expected: str = 'wrong\nwrong\nwrong\nright\n'
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_solve4(self) -> None:
        """Tests solve method
        """
        data4 = '2 3 4\n20 50 62\n3 4 7\n3 4 5\n0 0 0\n'
        with patch('sys.stdin', StringIO(data4)):
            sol = Solution(sys.stdin)
            sol.solve()
            expected: str = 'wrong\nwrong\nwrong\nright\n'
            self.assertEqual(sol.answer, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout: StringIO) -> None:
        """Tests main method
        """
        data = '2 3 4\n20 50 62\n3 4 7\n3 4 5\n0 0 0\n'
        with patch('sys.stdin', StringIO(data)):
            Solution.main()
            expected: str = 'wrong\nwrong\nwrong\nright\n'
            self.assertEqual(mock_stdout.getvalue(), expected)

    def test_data(self) -> None:
        """Tests data property
        """
        data = '2 3 4\n20 50 62\n3 4 7\n0 0 0\n'
        with patch('sys.stdin', StringIO(data)):
            sol = Solution(sys.stdin)
            self.assertEqual(
                sol.data, [[2, 3, 4], [20, 50, 62], [3, 4, 7]])
