"""Guess the number I am thinking of."""

import random


class Game:
    """Example of dice class."""

    low_number = 1
    high_number = 100
    the_number = None

    def __init__(self):
        """Init the object."""
        random.seed()

    def start(self):
        """Start the game and randomize a new number."""
        self.the_number = random.randint(self.low_number, self.high_number)

    def cheat(self):
        """Get the number."""
        return self.the_number

    def low(self):
        """Get the lowest number possible."""
        return self.low_number

    def high(self):
        """Get the highest number possible."""
        return self.high_number

    def guess(self, a_number):
        """
        Check it the guess is correct, higher or lower than the actual number.

        Raise an exception if the number is out of range.
        Raise an exception if the number is not an integer.
        """
        if not isinstance(a_number, int):
            raise TypeError("The number should be an integer.")

        if not self.low_number <= a_number <= self.high_number:
            raise ValueError("The number is higher/lower than max/min value.")

        msg = "Too Low"
        if a_number == self.the_number:
            msg = "Correct"
        elif a_number > self.the_number:
            msg = "Too High"

        return msg
