from deck import Deck
from game_player import Player
from game import WarCardGame

player = Player(input("Enter Player 1's name: "), Deck(is_empty=True))
mode = input("Enter game mode, PC(1) or other player (2): ")

if mode == "2":
    player2 = Player(input("Enter Player 2's name: "), Deck(is_empty=True))
else:
    player2 = Player("Computer", Deck(is_empty=True))

deck = Deck()
game = WarCardGame(player, player2, deck)

game.print_welcome_message()

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("\nReady?\nPress Enter to continue. Enter X to stop.")

    if answer.lower() == "x":
        break
