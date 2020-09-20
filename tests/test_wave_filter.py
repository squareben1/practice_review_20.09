import pytest
from src.wave_filter import wave_filter


def test_return_arr():
    assert wave_filter([10, 11]) == [10, 11]


def test_lower_limit():
    assert wave_filter([9, 10]) == [10, 10]
