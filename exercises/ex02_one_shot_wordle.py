"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730401544"

secret: str = ("python")

guess: str = str(input("What is your 6-letter guess? "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
s: str = ""

while len(guess) != 6:
    again: str = (input("That was not 6 letters! Try again: "))
    guess = again

while i < len(guess):
    if guess[i] == secret[i]:
        s = s + GREEN_BOX
    else:
        alternative: int = 0
        yellow: bool = False

        while yellow is False and alternative < len(secret):
            if guess[i] == secret[alternative]:
                yellow = True
            alternative += 1    

        if yellow is False:
            s = s + WHITE_BOX
        else:
            s = s + YELLOW_BOX
    i += 1

print(s)
if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")