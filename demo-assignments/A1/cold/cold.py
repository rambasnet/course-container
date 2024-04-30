#! /usr/bin/env python3
"""
Kattis cold problem.

Find the number of temperatures strictly less than zero.

Algorithm:
    1. Read the first line as number of temperatures
    2. Read the second line as space separated temperatures
    3. Split the second line into list of temperatures
    4. Iterate through the list and count the number of -ve temperatures
    5. Print the count
"""
__author__ = "Ram Basnet"
__date__ = "Oct 1, 2021"
__license__ = "MIT"

import sys
from typing import List


def answer(data: List[int]) -> int:
    """Count total number of -ve temeratures in data.

    Args:
        data (List[int]): List of integers as temperature

    Returns:
        int: count of -ve temps
    """
    count = 0
    for temp in data:
        if temp < 0:
            count += 1
    return count


def answer1(line: str) -> int:
    """Count total number of -ve temeratures in data.

    Args:
        line (str): integer temperatures as space separated string

    Returns:
        int: count of -ve temps
    """
    return line.count('-')


def solve1() -> None:
    """Reads input ans uses answer1 function.
    """
    _ = input()
    temps = input().strip()
    # print(f'{num=}; {temps=}', file=sys.stderr)
    print(answer1(temps))


def solve() -> None:
    """Reads input and parses the string as list of integer.
    """
    _ = sys.stdin.readline()
    # use list comprehension syntax
    temps = [int(temp) for temp in sys.stdin.readline().strip().split()]
    # print(f'{num=}; {temps=}', file=sys.stderr)
    print(answer(temps))


if __name__ == "__main__":
    solve()
    # solve1()
