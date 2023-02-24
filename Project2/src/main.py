from deck import Deck
from player import Player
from game import WarCardGame

"""
RULES HERE
"""

player = Player("AC", Deck(is_empty=True))
player2 = Player("Player 2", Deck(is_empty=True), is_computer=True)
deck = Deck()
