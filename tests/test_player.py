import unittest
from game import WarCardGame
from deck import Deck
from card import Card
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.player = Player("Anne-Claire", self.deck)

    def test_has_empty_deck(self):
        self.deck.add(Card("Spades", "Ace"))
        self.assertFalse(self.player.has_empty_deck())

    def test_draw(self):
        self.assertIsNotNone(self.player.draw_card())
        card = Card("Hearts", "Queen")
        self.deck._cards = [card]
        self.assertEqual(self.player.draw_card(), card)

    def test_add(self):
        card = Card("Spades", "Ace")
        self.player.add_card(card)
        self.assertIn(card, self.deck._cards)


if __name__ == "__main__":
    unittest.main()
