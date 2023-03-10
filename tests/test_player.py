"""
    Testing the Player class.

    This module contains unit tests for the Player class. The Player class represents a player in a card game.

"""
import unittest
from game.deck import Deck
from game.card import Card
from game.player import Player


class TestPlayer(unittest.TestCase):
    """Test case for the Player class."""

    def setUp(self):
        """Set up the test fixture."""
        self.deck = Deck()
        self.player = Player("Anne-Claire", self.deck)

    def test_has_empty_deck(self):
        """Test that the has_empty_deck method.

        Returns False when the player has cards in their deck.
        """
        self.deck.add(Card("Spades", "Ace"))
        self.assertFalse(self.player.has_empty_deck())

    def test_draw(self):
        """Test draw_card method so it returns a card.

        and removes it from the player's deck.
        """
        self.assertIsNotNone(self.player.draw_card())
        card = Card("Hearts", "Queen")
        self.deck._cards = [card]
        self.assertEqual(self.player.draw_card(), card)

    def test_add(self):
        """Test that the add_card method adds a card to the player's deck."""
        card = Card("Spades", "Ace")
        self.player.add_card(card)
        self.assertIn(card, self.deck._cards)


if __name__ == '__main__':
    unittest.main()
