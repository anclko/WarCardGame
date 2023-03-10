"""Class Intelligence."""
import random


class Intelligence:
    """class representing levels of intelligence for the PC mode.

    Attributes:
    None

    Methods:
    easy(deck): Returns random card from the deck.
    hard(deck): Returns the highest-value cards in the deck.
    """

    def easy(self, deck):
        """Select a random card from the deck.

        Args:
        deck (Deck): The deck of cards to choose from.

        Returns:
        The randomly selected card from the deck.
        """
        return random.choice(deck._cards)

    def hard(self, deck):
        """Select the highest-value card from the deck.

        Args:
        deck (Deck): The deck of cards to choose from.

        Returns:
        The card with the highest value in the deck.
        """
        return max(deck._cards)
