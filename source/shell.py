"""Importing."""

import cmd
import sys
from game import WarCardGame
from deck import Deck
from player import Player
from intelligence import Intelligence


class Shell(cmd.Cmd):
    """Shell class."""

    i = Intelligence()
    intro = "Type help or ? to list commands.\n"
    prompt = '> '

    def do_Start(self, _):
        """Start The Game."""
        player1 = Player(input("Enter your name: "), Deck(is_empty=True))
        mode = input("Enter game mode 1 for PC, 2 for 2nd Player: ")
        if mode == '2':
            p2 = Player(input("Enter opponent name: "), Deck(is_empty=True))
        else:
            p2 = Player("Computer", Deck(is_empty=True))

        # Create a new deck and game instance
        deck = Deck()
        game = WarCardGame(player1, p2, deck)

        if mode == '1':
            defficulty = input('what level do you want easy/hard? ')
            if defficulty.lower() != 'easy' and defficulty.lower() != 'hard':
                defficulty = input('what level do you want easy/hard? ')

            if defficulty.lower() == 'easy':
                self.i.easy(p2._deck)
            else:
                self.i.hard(p2._deck)

        # Start the game
        game.print_welcome_message()
        while not game.check_game_over():

            game.start_battle()
            game.print_stats()

            asnswer = input('press Enter to continue. Enter x to stop: ')
            if asnswer.lower() == 'x':
                break
            elif asnswer.lower() == 'restart':
                return self.do_restart(self)
            elif mode.lower() == '1':
                if asnswer.lower() == 'cheat':
                    return self.do_Cheat(self)

            if game.check_game_over():
                sys.exit()

    def do_Exit(self, _):
        """Exit the program."""
        print('Bye Bye!')
        return True

    def do_Restart(self, _):
        """Restart The Game."""
        return self.do_Start(self)

    def do_Cheat(self, _):
        """Win The Game By Cheating."""
        WarCardGame.cheat(self)
