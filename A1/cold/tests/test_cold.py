#!/ usr/bin/env python3

"""
separate test file for pytest
pytest recursively discovers all the files with test* and runs the
assert statements/function in them
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2021"
__license__ = "MIT"


import unittest.mock as mock
from io import StringIO
from cold import answer, answer1
from cold import solve1, solve


def test_answer() -> None:
    """Test cold.py answer function.
    """
    assert answer([12, -4, -56, -4544545, 64, 46464]) == 3


def test_answer1() -> None:
    """Test cold.py answer function.
    """
    assert answer([0, 453445, -1, -100, -45454, -44445]) == 4


def test_answer1_1() -> None:
    """Test cold.py answer1 function.
    """
    assert answer1('0 453445 -1 -100 -45454 -44445') == 4


@mock.patch('builtins.input', return_value='6\n0 453445 -1 -100 -45454 -44445\n')
@mock.patch('sys.stdout', new_callable=StringIO)
def test_solve_1(mock_print: StringIO, _: StringIO) -> None:
    """Test cold.py solve1 function.
    """
    solve1()
    assert mock_print.getvalue() == '4\n'


@mock.patch('sys.stdin.readline',
            return_value='9\n100 3343 0 453445 -134 -10054 -454543 -4444534 -345435\n')
@mock.patch('sys.stdout', new_callable=StringIO)
def test_solve_2(mock_print: StringIO, _: StringIO) -> None:
    """Test cold.py solve function.
    """
    solve()
    assert mock_print.getvalue() == '5\n'
