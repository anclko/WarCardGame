import unittest
from src.game import WarCardGame
from src.card import Card
from src.suit import Suit


class TestCard(unittest.TestCase):

    def test_value(self):
        """Create a Card object and assert it's value"""
        card = Card(Suit.HEARTS, 7)
        self.assertEqual(card.value, 7)

    def test_suit(self):
        """Create a Card object and assert it's suit"""
        card = Card(Suit.DIAMONDS, 10)
        self.assertEqual(card.suit, Suit.DIAMONDS)

    def test_special(self):
        """ Create a special card and assert it's 'specialness'"""
        card1 = Card(Suit.SPADES, 10)
        card2 = Card(Suit.CLUBS, 14)
        self.assertFalse(card1.is_special())
        self.assertTrue(card2.is_special())

    def test_lower(self):
        """ Create Card objects and compare high value"""
        card1 = Card(Suit.HEARTS, 7)
        card2 = Card(Suit.SPADES, 10)
        self.assertTrue(card1 < card2)

    def test_greater(self):
        """ Create Card objects and compare lower value"""
        card1 = Card(Suit.DIAMONDS, 12)
        card2 = Card(Suit.CLUBS, 5)
        self.assertTrue(card1 > card2)


if __name__ == '__main__':
    unittest.main()
