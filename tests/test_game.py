"""
This module contains a unittest test case for the WarCardGame class.

Tests:
- test_make_initial_decks: tests if the initial decks are created properly
- test_start_battle_player_wins: tests if player wins a battle
- test_start_battle_player2_wins: tests if player2 wins a battle
- test_start_battle_tie: tests if there is a tie in a battle
- test_start_war: tests if a war is won by player2
- test_start_war_not_enough_cards: tests if there are not enough cards in the deck to start a war
- test_start_war_enough_cards: tests if there are enough cards in the deck to start a war
- test_continue_war: tests if a war can be continued
- test_play_round: tests if a round is played properly
- test_play_round_war: tests if a round is played properly during a war
- test_check_game_over_not_empty_decks: tests if the game is not over with non-empty decks
- test_check_game_over_empty_player1_deck: tests if the game is over when player1's deck is empty
- test_check_game_over_empty_player2_deck: tests if the game is over when player2's deck is empty
- test_check_game_over_not_enough_cards_player1: tests if the game is over when player1 does not have enough cards for a war
- test_check_game_over_not_enough_cards_player2: tests if the game is over when player2 does not have enough cards for a war
- test_print_stats: tests if the print_stats() method works properly

"""


import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from game.game import WarCardGame
from game.player import Player
from game.card import Card
from game.deck import Deck

class TestWarCardGame(unittest.TestCase):
    """A unittest test case for the WarCardGame class."""
    
    def setUp(self):
        """Create a deck, two players, and a WarCardGame object for each test method."""
        self.deck = Deck()
        self.player = Player("Alice")
        self.player2 = Player("Bob")
        self.game = WarCardGame(self.player, self.player2, self.deck)

    def test_make_initial_decks(self):
        """Test that make_initial_decks method initializes each player's deck with 26 cards."""
        self.game.make_initial_decks()
        self.assertEqual(len(self.player.get_deck()), 26)
        self.assertEqual(len(self.player2.get_deck()), 26)

    def test_start_battle_player_wins(self):
        """Test that start_battle method correctly determines the winner of a battle when player 1 has the higher card."""
        self.player.add_card(Card(10))
        self.player2.add_card(Card(5))

        winner = self.game.start_battle()

        self.assertEqual(winner, WarCardGame.PLAYER)
        self.assertEqual(len(self.player.get_pile()), 2)

    def test_start_battle_player2_wins(self):
        """Test that start_battle method correctly determines the winner of a battle when player 2 has the higher card."""
        self.player.add_card(Card(5))
        self.player2.add_card(Card(10))

        winner = self.game.start_battle()

        self.assertEqual(winner, WarCardGame.PLAYER2)
        self.assertEqual(len(self.player2.get_pile()), 2)

    def test_start_battle_tie(self):
        """Test that start_battle method correctly determines a tie and initiates a war."""
        self.player.add_card(Card(5))
        self.player2.add_card(Card(5))

        self.deck.draw = MagicMock(side_effect=[
            Card(3),
            Card(9),
            Card(7),
            Card(2),
            Card(8),
            Card(6),
            Card(4),
            Card(10),
            Card(11),
            Card(2),
            Card(7),
            Card(8),
            Card(12),
            Card(9),
            Card(4),
            Card(6),
        ])

        winner = self.game.start_battle()

        self.assertEqual(winner, WarCardGame.TIE)
        self.assertEqual(len(self.player.get_pile()), 6)
        self.assertEqual(len(self.player2.get_pile()), 6)

    def test_start_war(self):
        """Test that start_war method correctly handles a war, with multiple cards played and a winner determined."""
        self.player.add_card(Card(5))
        self.player2.add_card(Card(4))
        self.player.add_card(Card(2))
        self.player2.add_card(Card(8))
        self.player.add_card(Card(7))
        self.player2.add_card(Card(3))
        self.player.add_card(Card(10))
        self.player2.add_card(Card(9))

        self.deck.draw = MagicMock(side_effect=[
            Card(3),
            Card(9),
            Card(7),
            Card(2),
        ])

        winner = self.game.start_war([Card(6), Card(5)])

        self.assertEqual(winner, WarCardGame.PLAYER2)
        self.assertEqual(len(self.player2.get_pile()), 8)

    def test_start_war_not_enough_cards(self):
        """Test that start_war method correctly handles the case where a player does not have enough cards to continue the war."""
        self.player1.deck.cards = []
        self.game.start_war([])
        self.assertTrue(self.game.check_game_over())

    def test_start_war_enough_cards(self):
        """Test that start_war method correctly handles the case where both players have enough cards to continue the war."""
        self.game.start_war([])
        self.assertEqual(self.player1.deck.size, 25)
        self.assertEqual(self.player2.deck.size, 25)

    @patch('builtins.input', return_value='y')
    def test_continue_war(self, mock_input):
        """Test that continue_war method correctly handles the case where the user chooses to continue the war."""
        self.game._player.deck.cards = [3, 4, 5]
        self.game._player2.deck.cards = [2, 4, 6]
        self.game.in_war = True
        self.game.continue_war()
        self.assertEqual(self.game._player.deck.size, 0)
        self.assertEqual(self.game._player2.deck.size, 6)

    def test_play_round(self):
        """Test that play_round method correctly plays a round of the game, with each player drawing a card and the winner determined."""
        self.game._player.deck.cards = [3, 4, 5]
        self.game._player2.deck.cards = [2, 4, 6]
        self.game.play_round()
        self.assertEqual(self.game.battleCards, [3, 2])
        self.assertEqual(self.game._player.deck.size, 2)
        self.assertEqual(self.game._player2.deck.size, 2)

    def test_play_round_war(self):
        """Test that play_round method correctly handles a round of the game during a war."""
        self.game._player.deck.cards = [3, 4, 5]
        self.game._player2.deck.cards = [3, 4, 6]
        self.game.play_round()
        self.assertEqual(self.game.battleCards, [3, 3, 'X', 'X', 4, 4])
        self.assertEqual(self.game._player.deck.size, 0)
        self.assertEqual(self.game._player2.deck.size, 0)

    def test_check_game_over_not_empty_decks(self):
        """Test that check_game_over method correctly returns False when both players have cards remaining in their decks."""
        self.assertFalse(self.game.check_game_over())

    def test_check_game_over_empty_player1_deck(self):
        """Test that check_game_over method correctly returns True when player 1's deck is empty."""
        self.game._player.deck.cards = []
        self.assertTrue(self.game.check_game_over())

    def test_check_game_over_empty_player2_deck(self):
        """Test that check_game_over method correctly returns True when player 2's deck is empty."""
        self.game._player2.deck.cards = []
        self.assertTrue(self.game.check_game_over())

    def test_check_game_over_not_enough_cards_player1(self):
        """Test that check_game_over method correctly returns True when player 1 does not have enough cards to continue a war."""
        self.game._player.deck.cards = [3, 4]
        self.game._player.in_war = True
        self.assertTrue(self.game.check_game_over())

    def test_check_game_over_not_enough_cards_player2(self):
        """Test that check_game_over method correctly returns True when player 2 does not have enough cards to continue a war."""
        self.game._player2.deck.cards = [3, 4]
        self.game._player2.in_war = True
        self.assertTrue(self.game.check_game_over())

    def test_print_stats(self):
        """Test that print_stats method correctly prints game statistics."""
        with patch('builtins.print') as mock_print:
            self.game.print_stats()
            mock_print.assert_called_with("Testing Print")

