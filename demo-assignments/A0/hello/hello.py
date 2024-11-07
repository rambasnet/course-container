#!/usr/bin/env python3

"""Kattis hello problem
"""
__author__ = "Ram Basnet"
__date__ = "Oct 1, 2023"
__license__ = "MIT"


def answer() -> str:
    """Returns Hello World!

    Returns:
        str: Hello World!
    """
    return "Hello World!"


def solve() -> None:
    """Solves the problem
    """
    print(answer())


if __name__ == "__main__":
    solve()  # pragma: no cover
