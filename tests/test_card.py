"""
This module contains unit tests for the Card class.

The Card class represents a playing card in a deck of cards.
It has a suit and a value. These unit tests verify the
correctness of the Card class and its methods.

The tests in this module include:

. test_value: tests that a Card object's value is set correctly
. test_suit: tests that a Card object's suit is set correctly
. test_special: tests that a special card is marked as special
and a non-special card is not
. test_lower: tests that a card with a lower value is less than
a card with a higher value
. test_greater: tests that a card with a higher value is greater
than a card with a lower value

"""


import unittest
from game.card import Card
from game.suit import Suit


class TestCard(unittest.TestCase):
    """Unit tests for the Card class."""

    def test_value(self):
        """Create a Card object and assert it's value."""
        card = Card(Suit.SYMBOLS["hearts"], 7)
        self.assertEqual(card.value, 7)

    def test_suit(self):
        """Create a Card object and assert it's suit."""
        card = Card(Suit.SYMBOLS["diamonds"], 10)
        self.assertEqual(card.suit, Suit.SYMBOLS["diamonds"])

    def test_special(self):
        """Create a special card and assert it's specialness."""
        card1 = Card(Suit.SYMBOLS["spades"], 10)
        card2 = Card(Suit.SYMBOLS["clubs"], 14)
        self.assertFalse(card1.is_special())
        self.assertTrue(card2.is_special())

    def test_lower(self):
        """Create Card objects and compare high value."""
        card1 = Card(Suit.SYMBOLS["hearts"], 7)
        card2 = Card(Suit.SYMBOLS["spades"], 10)
        self.assertTrue(card1 < card2)

    def test_greater(self):
        """Create Card objects and compare lower value."""
        card1 = Card(Suit.SYMBOLS["diamonds"], 12)
        card2 = Card(Suit.SYMBOLS["clubs"], 5)
        self.assertTrue(card1 > card2)


if __name__ == "__main__":
    unittest.main()
