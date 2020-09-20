import pytest
from src.wave_filter import *


def test_return_arr():
    assert wave_filter([10, 11]) == [10, 11]
