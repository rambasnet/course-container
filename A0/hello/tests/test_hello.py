#!/ usr/bin/env python3

"""
separate test file for pytest
pytest recursively discovers all the files with test* and runs the
assert statements in them
"""

import sys
from io import StringIO
from unittest.mock import patch
from hello import answer, solve


def test_answer() -> None:
    assert answer() == "Hello World!"


@patch('sys.stdout')
def test_solve(mock_stdout: 'sys.stdout') -> None:
    """Test solve function

    Args:
        mock_stdout (sys.stdout): sys.stdout is patched
    """
    with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        solve()
        assert mock_stdout.getvalue() == "Hello World!\n"
