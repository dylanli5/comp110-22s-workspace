"""Test for Dictionary Functions."""

__author__ = "730401544"

from exercises.ex06.dictionary import invert, favorite_color, count


def test_invert_none() -> None:
    """Test if input empty list yields a empty list."""
    input = {}
    assert invert(input) == {}


def test_invert_one() -> None:
    """Test if a one key and one value input list yields an invert list."""
    input = {"a": "b"}
    assert invert(input) == {"b": "a"}


def test_invert_two() -> None:
    """Test if a two keys and two values input list yields an invert list."""
    input = {"a": "b", "c": "d"}
    assert invert(input) == {"b": "a", "d": "c"}


def test_favorite_color_none() -> None:
    """Test if input empty list yields a empty str."""
    original = {}
    assert favorite_color(original) == ""


def test_favorite_color_one() -> None:
    """Test if input a tie for most popular color, return the color that appeared in the dictionary first."""
    original = {"Marc": "yellow", "Ezri": "blue"}
    assert favorite_color(original) == "yellow"


def test_favorite_color_two() -> None:
    """Test if input three color, the most appeared color shows."""
    original = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(original) == "blue"


def test_count() -> None:
    """Test if an empty list return a empty dict."""
    given = {}
    assert count(given) == {}


def test_count_one() -> None:
    """Test if a short list succeed."""
    given = ["1", "2", "1"]
    assert count(given) == {"1": 2, "2": 1}


def test_count_two() -> None:
    """Test if a longer list succeed."""
    given = ["1", "2", "1" ,"3", "1"]
    assert count(given) == {"1": 3, "2": 1, "3": 1}