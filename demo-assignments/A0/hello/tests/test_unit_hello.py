#! /usr/bin/env python3

"""unittest for hello solution"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from unittest.mock import patch
from io import StringIO
from hello import answer, solve


class TestHello(unittest.TestCase):
    """ Test hello.py solution.
    """

    def test1_answer(self) -> None:
        """Test hello.py answer function"""
        self.assertEqual(answer(), 'Hello World!', "Test failed...")

    def test_solve(self) -> None:
        """Test hello.py solve function"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            solve()
            self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')
        self.assertEqual(answer(), 'Hello World!', "Test failed...")
