#! /usr/bin/env python3

"""unittesting cold.py solution
"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from typing import List
from hypothesis import given
from hypothesis import strategies as some
from hypothesis import settings, Verbosity
from cold import answer, answer1


class TestCold(unittest.TestCase):
    """ Test cold.py solution
    """

    def test1_answer(self) -> None:
        """Test cold.py answer function"""
        data = [12, -4, -56, -4544545, 64, 46464]
        self.assertEqual(answer(data), 3, 'broken')

    def test2_answer(self) -> None:
        """Test cold.py answer function"""
        self.assertEqual(
            answer([0, 453445, -1, -100, -45454, -44445]), 4, 'borken')

    def test3_answer(self) -> None:
        """ Test cold.py answer1 function"""
        self.assertEqual(
            answer1('0 453445 -1 -100 -45454 -44445'), 4, 'broken')

    def neg_int_count(self, temps: List[int]) -> int:
        """ Count number of negative integers in temps"""
        neg_count = 0
        for temp in temps:
            if temp < 0:
                neg_count += 1
        return neg_count

    @given(some.lists(some.integers()))
    def test4_answer(self, nums: List[int]) -> None:
        """ Test cold.py answer function with random integers"""
        expected = self.neg_int_count(nums)
        ans = answer(nums)
        self.assertEqual(ans, expected)

    # follow input integer ranges provided in the problem statement
    @settings(max_examples=200, verbosity=Verbosity.verbose,
              derandomize=True)
    @given(some.lists(some.integers(min_value=-
                                    1_000_000, max_value=1_000_000),
                      max_size=100))
    def test5_answer(self, nums: List[int]) -> None:
        """ Test cold.py answer function with random integers"""
        expected = self.neg_int_count(nums)
        ans = answer(nums)
        self.assertEqual(ans, expected)

    @settings(max_examples=200,
              derandomize=True)
    @given(some.lists(some.integers(min_value=-
                                    1_000_000, max_value=1_000_000),
                      max_size=100))
    def test6_answer1(self, nums: List[int]) -> None:
        """ Test cold.py answer1 function with random integers"""
        str_nums = ' '.join(map(str, nums))
        expected = self.neg_int_count(nums)
        ans = answer1(str_nums)
        self.assertEqual(ans, expected)
