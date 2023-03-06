from src.suit import Suit
from src.game import WarCardGame
import unittest

class TestSuit(unittest.TestCase):

    def test_description(self):
        suit = Suit("spade")
        self.assertEqual(suit.description, "spade")

    def test_symbol(self):
        suit = Suit("diamonds")
        self.assertEqual(suit.symbol, "♦")

    def test_upperdescription(self):
        suit = Suit("HEARTS")
        self.assertEqual(suit.description, "HEARTS")

    def test_unknownDescription(self):
        with self.assertRaises(KeyError):
            Suit("unknown")

if __name__ == '__main__':
    unittest.main()