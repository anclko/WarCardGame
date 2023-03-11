"""Test case class for testing the `Deck` class.

This test case includes four test methods that test the
functionalities of the `Deck` class.

Methods:
test_build -- Test the `build` method of the `Deck` class.
test_shuffle -- Test the `shuffle` method of the `Deck` class.
test_draw -- Test the `draw` method of the `Deck` class.
test_add -- Test the `add` method of the `Deck` class.
"""


import unittest
from game.card import Card
from game.suit import Suit
from game.deck import Deck


class TestDeck(unittest.TestCase):
    """Testing the deck class."""

    def test_build(self):
        """Test build method."""
        deck = Deck()
        self.assertEqual(deck.size, 52)

    def test_shuffle(self):
        """Testing the shuffle method."""
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        deck2.shuffle()
        self.assertNotEqual(deck1._cards, deck2._cards)

    def test_draw(self):
        """Testing the draw method."""
        deck = Deck()
        card = deck.draw()
        self.assertIsInstance(card, Card)

    def test_add(self):
        """Testing the add method."""
        deck = Deck()
        card = Card(Suit("hearts"), 2)
        deck.add(card)
        self.assertEqual(deck.size, 53)
        self.assertEqual(deck._cards[0], card)


if __name__ == "__main__":
    unittest.main()
