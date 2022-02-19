"""`list` Utility Functions."""

__author__ = "730401544"


def only_evens(original: list[int]) -> list[int]:
    """Construct list of evens."""
    result: list[int] = list()
    i: int = 0
    while i < len(original):
        if original[i] % 2 == 0:
            result.append(original[i])
        i += 1
    return result


def sub(original: list[int], start: int, end: int) -> list[int]:
    """Generate a List which is a subset of the given list, between the specified start index and the end index."""
    result: list[int] = list()
    i: int 
    if start < 0:
        start = 0
    if end > len(original):
        end = len(original)
    i = start
    while i < end:
        result.append(original[i])
        i += 1
    return result


def concat(first: list[int], second: list[int]) -> list[int]:
    """Generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    result: list[int] = list()
    i: int = 0
    count: int = 0
    while i < len(first):
        result.append(first[i])
        i += 1
    while count < len(second):
        result.append(second[count]) 
        count += 1
    return result
