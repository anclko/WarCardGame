import unittest
from src.deck import Deck
from src.card import Card
from src.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player = Player("Anne-Claire", self.deck)

    def test_has_empty_deck(self):
        self.assertTrue(self.player.has_empty_deck())
        self.deck.add(Card("Spades", "Ace"))
        self.assertFalse(self.player.has_empty_deck())

    def test_draw(self):
        self.assertIsNone(self.player.draw_card())
        self.deck.add(Card("Diamonds", "Jack"))
        self.assertEqual(self.player.draw_card(), Card("Diamonds", "Jack"))

    def test_add(self):
        card = Card("Spades", "Ace")
        self.player.add_card(card)
        self.assertIn(card, self.deck.cards)

if __name__ == '__main__':
    unittest.main()
