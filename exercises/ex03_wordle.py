"""EX03 - Structured Wordle."""

__author__ = "730401544"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(search_in: str, search: str) -> bool:
    """Given a string, see if a character is in this sring."""
    assert len(search) == 1
    i: int = 0
    while i < len(search_in):
        if search_in[i] == search:
            return True
        i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Given a guess, see each character matches the secret."""
    assert len(guess) == len(secret)
    i: int = 0
    s: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            s = s + GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                s = s + YELLOW_BOX
            else:
                s = s + WHITE_BOX
        i += 1
    return s


def input_guess(length: int) -> str:
    """Given a expected length of guess, prompt the guess."""
    guess: str = str(input(f"Enter a {length} character word: "))
    while len(guess) != length:
        again: str = str(input(f"That wasn't {length} chars! Try again: "))
        guess = again
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = ("codes")
    i: int = 1
    win: bool = False
    while i <= 6 and win is False:
        print(f"=== Turn {i}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            win = True
        i += 1
            
    if i > 6:
        print("X/6 - Sorry, try again tomorrow!")
    else:
        print(f"You won in {i-1}/6 turns!")


if __name__ == "__main__":
    main()