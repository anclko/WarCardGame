"""This module contains test case for the Intelligence class of the game.

It tests functionality of the easy and hard methods of the Intelligence class.
"""
import unittest
from game.card import Card
from game.deck import Deck
from game.intelligence import Intelligence

i = Intelligence()


class IntelligenceTestCase(unittest.TestCase):
    """Test case class for the Intelligence class."""

    def test_easy(self):
        """Test the easy method of the Intelligence class."""
        deck = Deck()
        deck._cards = [Card("Spades", "Q"), Card("Diamonds", "4")]
        card = i.easy(deck)

        self.assertTrue(card, deck._cards)

    def test_hard(self):
        """Test the hard method of the Intelligence class."""
        deck = Deck()
        LowerValueCard = Card("Hearts", "7")
        HigherValueCard = Card("Clubs", "K")
        deck._cards = [LowerValueCard, HigherValueCard]

        card = i.hard(deck)

        self.assertEqual(card, HigherValueCard)


if __name__ == '__main__':
    """For running in vscode."""
    unittest.main()
