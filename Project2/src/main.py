from deck import Deck
from player import Player
from game import WarCardGame

"""
RULES HERE
"""

player = Player("AC", Deck(is_empty=True))
player2 = Player("Player 2", Deck(is_empty=True), is_computer=True)
deck = Deck()
warGame = WarCardGame(player, player2, deck)

warGame.print_welcome_message()

while not warGame.check_game_over():
    warGame.start_battle()
    warGame.print_stats()

    choice = input("\nReady?\nPress Enter to continue. Enter X to stop.")

    if choice.lower() == "x":
        break

