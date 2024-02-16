"""
Testing Solution class
"""

__author__ = "Ram Basnet"
__date__ = "2023/1/1"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Ram Basnet"


import unittest
from unittest.mock import patch
from io import StringIO
from main import Main, main


class TestMain(unittest.TestCase):
    """
    Testing Singleton Main class
    """

    @patch('sys.stdout', new_callable=StringIO)
    def test_solve(self, mock_stdout: StringIO) -> None:
        """
        Tests solve method
        """
        my_main: 'Main' = Main.get_instance()
        my_main.solve()
        self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')

    def test_get_instance(self) -> None:
        """
        Tests get_instance method
        """
        my_main: 'Main' = Main.get_instance()
        self.assertIs(my_main.get_instance(), my_main)

    def test_exeception(self) -> None:
        """
        Tests exception with multiple instances
        """
        _ = Main.get_instance()
        self.assertRaises(NameError, Main)

    def test_main_static(self) -> None:
        """
        Tests main staticmethod
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # call the static method
            Main.main()
            self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')

    def test_main_global(self) -> None:
        """
        Tests main global function
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # call the global function
            main()
            self.assertEqual(mock_stdout.getvalue(), 'Hello World!\n')
