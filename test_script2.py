import pytest
from script2 import add_numbers

def test():
    assert add_numbers(1, 2) == 3
    assert add_numbers(10, 20) == 30
    assert add_numbers(10, -2) == 8
