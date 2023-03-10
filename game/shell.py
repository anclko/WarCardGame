"""Importing."""

import cmd
from game.game import WarCardGame
from game.deck import Deck
from game.player import Player
from game.intelligence import Intelligence


class Shell(cmd.Cmd):
    """Shell class."""

    i = Intelligence()
    intro = "Type help or ? to list commands.\n"
    prompt = "> "

    def do_Start(self, _):
        """Start The Game."""
        # PLAYER NAME #
        while True:
            try:
                player1_name = input("Enter your name: ")
                if not player1_name.isalpha():
                    raise ValueError("Name should only contain letters.")
                break
            except ValueError as e:
                print(e)

        # GAME MODE #
        while True:
            try:
                mode = input("Enter game (1) for PC, (2) for 2nd Player: ")
                if mode != "1" and mode != "2":
                    raise ValueError("Invalid choice. Try again!")
                break
            except ValueError as e:
                print(e)

        if mode == "2":
            while True:
                try:
                    p2_name = input("Enter opponent name: ")
                    if not p2_name.isalpha():
                        raise ValueError("Name should only contain letters.")
                    break
                except ValueError as e:
                    print(e)
            p2 = Player(p2_name, Deck(is_empty=True))
        else:
            p2 = Player("RacoonChan", Deck(is_empty=True))

        player1 = Player(player1_name, Deck(is_empty=True))

        # Create Deck and Player instance
        deck = Deck()
        game = WarCardGame(player1, p2, deck)

        # GAME MODE
        if mode == "1":
            while True:
                try:
                    dif_lvl = input("Select Difficulty: Easy(1) or Hard(2): ")
                    if dif_lvl != "1" and dif_lvl != "2":
                        raise ValueError("Invalid choice. Try again!")
                    break
                except ValueError as e:
                    print(e)

            if dif_lvl.lower() == 1:
                self.i.easy(p2._deck)
            else:
                self.i.hard(p2._deck)

        # Start the game
        game.print_welcome_message()
        while not game.check_game_over():
            game.start_battle()
            game.print_stats()

            answer = input("press Enter to continue. Enter x to stop: ")
            if answer.lower() == "x":
                break
            elif answer.lower() == "restart":
                return self.do_restart(self)
            elif mode.lower() == "1":
                if answer.lower() == "cheat":
                    return self.do_Cheat(self)

    def do_Exit(self, _):
        """Exit the program."""
        print("Bye Bye!")
        return True

    def do_Restart(self, _):
        """Restart The Game."""
        return self.do_Start(self)

    def do_Cheat(self, _):
        """Win The Game By Cheating."""
        WarCardGame.cheat(self)
