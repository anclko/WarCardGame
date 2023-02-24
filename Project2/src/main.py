from deck import Deck
from player import Player
from war_card_game import WarCardGame

player = Player("AC", Deck(is_empty=True))
player2 = Player("Player 2", Deck(is_empty=True), is_computer=True)
deck = Deck()

game = WarCardGame(player, player2, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nReady?\nPress Enter to continue. Enter X to stop.")

    if answer.lower() == "x":
        break
