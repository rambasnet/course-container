#! /usr/bin/env python3

"""unittest for hello solution"""

__author__ = "Ram Basnet"
__copyright__ = "Copyright 2020"
__license__ = "MIT"

import unittest
from hello import answer


class TestHello(unittest.TestCase):
    """ Test hello.py solution.
    """

    def test1_answer(self) -> None:
        """Test hello.py answer function"""
        self.assertEqual(answer(), 'Hello World!', "Test failed...")


if __name__ == "__main__":
    unittest.main(verbosity=2)
