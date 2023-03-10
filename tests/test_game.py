import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from game.game import WarCardGame
from game.player import Player
from game.card import Card
from game.deck import Deck

class TestWarCardGame(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player = Player("Alice")
        self.player2 = Player("Bob")
        self.game = WarCardGame(self.player, self.player2, self.deck)

    def test_make_initial_decks(self):
        self.game.make_initial_decks()
        self.assertEqual(len(self.player.get_deck()), 26)
        self.assertEqual(len(self.player2.get_deck()), 26)

    def test_start_battle_player_wins(self):
        self.player.add_card(Card(10))
        self.player2.add_card(Card(5))

        winner = self.game.start_battle()

        self.assertEqual(winner, WarCardGame.PLAYER)
        self.assertEqual(len(self.player.get_pile()), 2)

    def test_start_battle_player2_wins(self):
        self.player.add_card(Card(5))
        self.player2.add_card(Card(10))

        winner = self.game.start_battle()

        self.assertEqual(winner, WarCardGame.PLAYER2)
        self.assertEqual(len(self.player2.get_pile()), 2)

    def test_start_battle_tie(self):
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
        self.player1.deck.cards = []
        self.game.start_war([])
        self.assertTrue(self.game.check_game_over())

    def test_start_war_enough_cards(self):
        self.game.start_war([])
        self.assertEqual(self.player1.deck.size, 25)
        self.assertEqual(self.player2.deck.size, 25)

    @patch('builtins.input', return_value='y')
    def test_continue_war(self, mock_input):
        self.game._player.deck.cards = [3, 4, 5]
        self.game._player2.deck.cards = [2, 4, 6]
        self.game.in_war = True
        self.game.continue_war()
        self.assertEqual(self.game._player.deck.size, 0)
        self.assertEqual(self.game._player2.deck.size, 6)

    def test_play_round(self):
        self.game._player.deck.cards = [3, 4, 5]
        self.game._player2.deck.cards = [2, 4, 6]
        self.game.play_round()
        self.assertEqual(self.game.battleCards, [3, 2])
        self.assertEqual(self.game._player.deck.size, 2)
        self.assertEqual(self.game._player2.deck.size, 2)

    def test_play_round_war(self):
        self.game._player.deck.cards = [3, 4, 5]
        self.game._player2.deck.cards = [3, 4, 6]
        self.game.play_round()
        self.assertEqual(self.game.battleCards, [3, 3, 'X', 'X', 4, 4])
        self.assertEqual(self.game._player.deck.size, 0)
        self.assertEqual(self.game._player2.deck.size, 0)

    def test_check_game_over_not_empty_decks(self):
        self.assertFalse(self.game.check_game_over())

    def test_check_game_over_empty_player1_deck(self):
        self.game._player.deck.cards = []
        self.assertTrue(self.game.check_game_over())

    def test_check_game_over_empty_player2_deck(self):
        self.game._player2.deck.cards = []
        self.assertTrue(self.game.check_game_over())

    def test_check_game_over_not_enough_cards_player1(self):
        self.game._player.deck.cards = [3, 4]
        self.game._player.in_war = True
        self.assertTrue(self.game.check_game_over())

    def test_check_game_over_not_enough_cards_player2(self):
        self.game._player2.deck.cards = [3, 4]
        self.game._player2.in_war = True
        self.assertTrue(self.game.check_game_over())

    def test_print_stats(self):
        with patch('builtins.print') as mock_print:
            self.game.print_stats()
            mock_print.assert_called_with("Testing Print")

