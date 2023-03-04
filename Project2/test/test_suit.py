from suit import Suit
from game import WarCardGame
import unittest

class TestSuit(unittest.TestCase):

    def test_description(self):
        suit = Suit("spades")
        self.assertEqual(suit.description, "spades")

    def test_symbol(self):
        suit = Suit("diamonds")
        self.assertEqual(suit.symbol, "♦")

    def test_upperdescription(self):
        suit = Suit("HEARTS")
        self.assertEqual(suit.description, "HEARTS")

    def test_unknownDescription(self):
        with self.assertRaises(KeyError): # <-- we dont have a method that raises an error, this is not needed
            Suit("unknown")

if __name__ == '__main__':
    unittest.main()
