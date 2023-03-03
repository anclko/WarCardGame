"""Importing."""
import unittest
from src.game import WarCardGame
from src.card import Card
from src.suit import Suit
from src.deck import Deck


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


if __name__ == '__main__':
    unittest.main()
