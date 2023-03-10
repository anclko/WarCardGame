"""Doc."""


import random

# CPU side and cheating implementation in this
# When the computer is playing, it should have some type of
# intelligence for playing the game. There might be several
# settings för the level of intelligence for the computer playing.
# These should be configurable by the user while playing.


class Intelligence:
    """Doc."""

    def easy(self, deck):
        """Doc."""
        return random.choice(deck._cards)

    def hard(self, deck):
        """Doc."""
        return max(deck._cards)
