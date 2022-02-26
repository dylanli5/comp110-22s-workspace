"""Tests for Utility function."""

__author__ = "730401544"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test if sa empty list yields a empty list."""
    original: list[int] = []
    assert only_evens(original) == []


def test_only_evens_single_item() -> None:
    """Test if a single even numnber list yields a list of this even number."""
    original: list[int] = [2]
    assert only_evens(original) == [2]


def test_only_evens_two_item() -> None:
    """Test if a list with a even numnber and a odd number list yields a list of the even number."""
    original: list[int] = [4, 5]
    assert only_evens(original) == [4]


def test_sub_empty() -> None:
    """Test if a empty list yields a empty list."""
    original: list[int] = []
    start = 4
    end = 1
    assert sub(original, start, end) == []


def test_sub_empty_2() -> None:
    """Test if a list with lenth of 0, start and end = 0 yields a empty list."""
    original: list[int] = []
    start = 0
    end = 0
    assert sub(original, start, end) == []


def test_sub_1() -> None:
    """Test if a list with 4 items, the start of 1 and the end of 3 yiels the second and the third item."""
    original: list[int] = [10, 20, 30, 40]
    start = 1
    end = 3
    assert sub(original, start, end) == [20, 30]


def test_sub_2() -> None:
    """Test if a list with 4 items, when the start is less than 0, it starts from 0."""
    original: list[int] = [10, 20, 30, 40]
    start = -1
    end = 5
    assert sub(original, start, end) == [10, 20, 30, 40]


def test_concat_empty() -> None:
    """Test if two empty lists yields a empty list."""
    first: list[int] = list()
    second: list[int] = list()
    assert concat(first, second) == []


def test_concat_1() -> None:
    """Test if two lists yields a list accordingly."""
    first: list[int] = [1, 2, 3]
    second: list[int] = [4, 5, 6]
    assert concat(first, second) == [1, 2, 3, 4, 5, 6]


def test_concat_2() -> None:
    """Test if two lists yields a list according to the sequence of the list."""
    first: list[int] = [4, 5, 6]
    second: list[int] = [1, 2, 3]
    assert concat(first, second) == [4, 5, 6, 1, 2, 3]