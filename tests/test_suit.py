"""Testing suit class."""
from game.suit import Suit
import unittest


class TestSuit(unittest.TestCase):
    """Doc."""

    def test_description(self):
        """Test that the description of a suit is set correctly."""
        suit = Suit("spade")
        self.assertEqual(suit.description, "spades")

    def test_symbol(self):
        """Test that the symbol of a suit is set correctly."""
        suit = Suit("diamonds")
        self.assertEqual(suit.symbol, "♦")

    def test_upperdescription(self):
        """Test that the description of a suit is case-insensitive."""
        suit = Suit("HEARTS")
        self.assertEqual(suit.description, "HEARTS")

    def test_unknownDescription(self):
        """Test error raised when creating a Suit with unknown description."""
        with self.assertRaises(KeyError):
            Suit("unknown")


if __name__ == '__main__':
    unittest.main()
