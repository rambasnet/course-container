"""
Kattis ABC class for Kattis problems
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Kattis(ABC):
    """
    Solution ABC class for Kattis problems
    """

    def __init__(self, data_source: Any) -> None:
        """Constructor

        Args:
            data_source (Any): input data source object
        """
        self._input_source: Any = data_source
        self._data: Any = None
        self._answer: Any = None

    @abstractmethod
    def read_input(self) -> None:
        """
        Reads the data from the given source
        """

    @property
    @abstractmethod
    def data(self) -> Any:
        """
        Returns the data
        """

    @property
    @abstractmethod
    def answer(self) -> Any:
        """
        Returns the answer
        """

    @abstractmethod
    def solve(self) -> None:
        """
        Solves the problem
        """

    @abstractmethod
    def print_answer(self) -> None:
        """
        Prints the answer
        """
