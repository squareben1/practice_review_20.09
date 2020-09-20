import pytest
from src.wave_filter import wave_filter


def test_return_arr():
    assert wave_filter([10, 11]) == [10, 11]


def test_lower_limit():
    assert wave_filter([9, 10]) == [10, 10]


def test_upper_limit():
    assert wave_filter([10, 21]) == [10, 20]


def test_user_assign_lower_limit():
    assert wave_filter([11, 21], 15) == [15, 20]


def test_user_assign_upper_limit():
    assert wave_filter([11, 21], 15, 25) == [15, 21]
