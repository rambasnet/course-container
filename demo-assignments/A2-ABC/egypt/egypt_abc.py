"""
Solution class that extends Kattis ABC class to solve the problem
"""

from __future__ import annotations

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"

from typing import Any, List
import sys
from kattis import Kattis
from triangle import Triangle


class Solution(Kattis):
    """
    Solution concrete class
    """

    def __init__(self, input_source: Any = sys.stdin) -> None:
        """ Constructor
        """
        super().__init__(input_source)
        self._data: List[List[int]] = []
        self._triangles: List[Triangle] = []
        self._answer: List[str] = []
        self.read_input()

    def read_input(self) -> None:
        """Reads the data from the given source.
        """
        data = self._input_source.readlines()
        # ignore the last line: 0, 0, 0
        self._data = [list(map(int, data[i].split()))
                      for i in range(len(data) - 1)]
        for a, b, c in self._data:
            self._triangles.append(Triangle(a, b, c))
        # print(self._triangles)

    @property
    def data(self) -> List[List[int]]:
        """ Data property
        Returns:
            List[List[int]]: data
        """
        return self._data

    @property
    def answer(self) -> str:
        """Answer property

        Returns:
            str: answer
        """
        return '\n'.join([str(t) for t in self._answer])

    def solve(self) -> None:
        """Solves the problem
        """
        for t in self._triangles:
            self._answer.append('right' if t.is_right_angled() else 'wrong')

        self._answer.append('')

    def print_answer(self) -> None:
        """
        Prints the answer
        :return: None
        """
        sys.stdout.write(self.answer)

    @staticmethod
    def main() -> None:
        """
        Main method
        """
        solution = Solution(sys.stdin)
        solution.solve()
        solution.print_answer()


if __name__ == "__main__":
    Solution.main()  # pragma: no cover
