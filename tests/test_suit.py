"""Doc."""
from game.suit import Suit
import unittest


class TestSuit(unittest.TestCase):
    """Doc."""

    def test_description(self):
        """Doc."""
        suit = Suit("spade")
        self.assertEqual(suit.description, "spade")

    def test_symbol(self):
        """Doc."""
        suit = Suit("diamonds")
        self.assertEqual(suit.symbol, "♦")

    def test_upperdescription(self):
        """Doc."""
        suit = Suit("HEARTS")
        self.assertEqual(suit.description, "HEARTS")

    def test_unknownDescription(self):
        """Doc."""
        with self.assertRaises(KeyError):
            Suit("unknown")


if __name__ == "__main__":
    unittest.main()
