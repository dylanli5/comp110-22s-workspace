"""Example of a funciton that searches through a list."""


from pip import main


def mian() -> None:
    print(contains("Kevin Bacon", ["Kane West", "Pete Davidson"]))
# Define a function named contains
# Two parameters:
# 1. needle - the string we're searching for
# 2. haystack - the list we're searching through


def contains(needle: str, haystack: list[str]) -> bool:
    # Algorithm:
    #  For each iterm in the haystack:
    #   Test if it is equal to the needle
    #    If so, return True
    for item in haystack:
        if item == needle:
            return True
#  After testing all items, return False, because not found
# Returns true if needle in haystack, false otherwise
    return False


if __name__ == "__main__":
    main()
# else:
#     print(__name__)