"""Dictionary Functions."""

__author__ = "730401544"


def invert(input: dict[str, str]) -> dict[str, str]:
    """The keys of input would be the value of the output."""
    a: list[str] = list()
    b: list[str] = list()
    output: dict[str, str] = {}
    for key in input:
        a.append(input[key])
        b.append(key)
    i: int = 0
    while i < len(a):
        output[a[i]] = b[i]
        i += 1
    return output
    # output: dict[str, str] = {}
    # for key in input:
    #     output[key] = key
    # return output


def favorite_color(original: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    color: list[str] = list()
    for key in original:
        color.append(original[key])
    i: int = 0
    max: int = 0
    color_max: str = ""
    while i < len(color):
        count: int = 0
        s: str = color[i]
        x: int = 0
        while x < len(color):
            if color[i] == color[x]:
                count += 1
            x += 1
        if count > max:
            color_max = s
            max = count 
        i += 1
    return color_max


def count(given: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    i: int = 0
    while i < len(given):
        unique: str = ""
        count: int = 0
        if given[i] in result:
            result[given[i]] += 1
        else:
            unique = given[i]
            count = 1
            result[unique] = count
        i += 1
    
    return result 
