"""
This module contains a unittest test case for the WarCardGame class.

Tests:
- test_make_initial_decks: tests if the initial decks are created properly
- test_start_battle_player_wins: tests if player wins a battle
- test_start_battle_player2_wins: tests if player2 wins a battle
- test_start_battle_tie: tests if there is a tie in a battle
- test_start_war: tests if a war is won by player2
- test_start_war_not_enough_cards: tests if there are not
  enough cards in the deck to start a war
- test_start_war_enough_cards: tests if there are enough
  cards in the deck to start a war
- test_continue_war: tests if a war can be continued
- test_play_round: tests if a round is played properly
- test_play_round_war: tests if a round is played properly during a war
- test_check_game_over_not_empty_decks: tests if the game is not over with
  non-empty decks
- test_check_game_over_empty_player1_deck: tests if the game is
  over when player1's deck is empty
- test_check_game_over_empty_player2_deck: tests if the game is
  over when player2's deck is empty
- test_check_game_over_not_enough_cards_player1: tests if the game is
  over when player1 does not have enough cards for a war
- test_check_game_over_not_enough_cards_player2: tests if the game is
  over when player2 does not have enough cards for a war
- test_print_stats: tests if the print_stats() method works properly.
"""


import unittest
from game.game import WarCardGame
from game.player import Player
from game.card import Card
from game.deck import Deck


class TestWarCardGame(unittest.TestCase):
    """Unittest test case for the WarCardGame class."""

    def setUp(self):
        """Seting up objects."""
        self.player1 = Player("Ibrahim", Deck(is_empty=True))
        self.player2 = Player("Anne-Clair :)", Deck(is_empty=True))
        self.deck = Deck()
        self.game = WarCardGame(self.player1, self.player2, self.deck)

    def test_get_round_winner(self):
        """Testing round winner."""
        card1 = Card("Hearts", 5)
        card2 = Card("Diamonds", 8)
        card3 = Card("Spades", 2)
        self.assertEqual(self.game.get_round_winner(card1, card2),
                         WarCardGame.PLAYER2)
        self.assertEqual(self.game.get_round_winner(card2, card3),
                         WarCardGame.PLAYER)
        self.assertEqual(self.game.get_round_winner(card1, card1),
                         WarCardGame.TIE)

    def test_get_cards_won(self):
        """Testing cards won method."""
        card1 = Card("Hearts", 5)
        card2 = Card("Diamonds", 8)
        card3 = Card("Clubs", 10)
        card4 = Card("Hearts", 9)
        cards_won = self.game.get_cards_won(card1, card2, card3, card4)
        self.assertEqual(cards_won, [card1, card2, card3, card4])

    def test_add_cards_to_players(self):
        """Testing adding cards to a player."""
        cards = [Card("Hearts", 5), Card("Diamonds", 8), Card("Clubs", 10)]
        self.game.add_cards_to_players(self.player1, cards)
        self.assertEqual(self.player1.deck.size, 29)

    def test_start_war(self):
        """Testing Start war method."""
        cards = [Card("Hearts", 5), Card("Diamonds", 8), Card("Clubs", 10)]
        self.game.start_war(cards)
        self.assertEqual(self.player1.deck.size(), 22)
        self.assertEqual(self.player2.deck.size(), 22)

    def test_check_game_over(self):
        """Testing if the game is over."""
        self.assertFalse(self.game.check_game_over())


if __name__ == '__main__':
    unittest.main()
