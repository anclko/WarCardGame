"""Unit testing."""
import unittest
from game import game


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = game.Game()
        exp = game.Game
        self.assertIsInstance(res, exp)

    def test_start_the_game(self):
        """Roll a dice and check value is in bounds."""
        the_game = game.Game()
        the_game.start()

        res = the_game.the_number
        exp = the_game.low_number <= res <= the_game.high_number
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
