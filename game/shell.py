"""Class Shell."""

import cmd
from game.game import WarCardGame
from game.deck import Deck
from game.player import Player
from game.intelligence import Intelligence


class Shell(cmd.Cmd):
    """A command-line interface for playing War card game.

    This class provides a command-line interface for playing the War card game.
    It allows the player to start a new game,
    select the game mode and difficulty
    level, and play the game by entering commands.
    The available commands include
    starting a new game, restarting the game, cheating to win the game, and
    exiting the program.

    Attributes:
    i (Intelligence): An instance of the Intelligence class that can be used
    to control the PC's gameplay.
    intro (str): The welcome message that is displayed when the game starts.
    prompt (str): The prompt symbol that is displayed when waiting for
    user input.
    """

    i = Intelligence()
    intro = "Type help or ? to list commands.\n"
    prompt = '> '

    def do_Start(self, _):
        """Start a new game of WarCardGame.

        The player is prompted to enter their name, and whether they want to
        play against the computer or another player.
        If playing against another player, they are prompted to enter the
        opponent's name.
        The game difficulty level is also prompted for, if playing
        against the computer.

        Once the game is set up, the game is started, and the player
        is prompted to press Enter to continue each turn.
        If the player enters 'x', the game ends.
        If the player enters 'restart', the game restarts.
        If the player is playing against the computer and enters 'cheat',
        the computer player's deck is revealed.

        Returns:
        None.
        """
        # PLAYER NAME #
        while True:
            try:
                player1_name = input("Enter your name: ")
                if not player1_name.isalpha():
                    raise ValueError("Name should only contain letters.")
                break
            except ValueError as error:
                print(error)

        # GAME MODE #
        while True:
            try:
                mode = input("Enter game (1) for PC, (2) for 2nd Player: ")
                if mode != "1" and mode != "2":
                    raise ValueError("Invalid choice. Try again!")
                break
            except ValueError as error:
                print(error)

        if mode == "2":
            while True:
                try:
                    p2_name = input("Enter opponent name: ")
                    if not p2_name.isalpha():
                        raise ValueError("Name should only contain letters.")
                    break
                except ValueError as error:
                    print(error)
            p_2 = Player(p2_name, Deck(is_empty=True))
        else:
            p_2 = Player("RacoonChan", Deck(is_empty=True))

        player1 = Player(player1_name, Deck(is_empty=True))

        # Create Deck and Player instance
        deck = Deck()
        game = WarCardGame(player1, p_2, deck)

        # GAME MODE
        if mode == '1':
            while True:
                try:
                    dif_lvl = input('Select Difficulty: Easy(1) or Hard(2): ')
                    if dif_lvl != "1" and dif_lvl != "2":
                        raise ValueError("Invalid choice. Try again!")
                    break
                except ValueError as error:
                    print(error)

            if dif_lvl.lower() == 1:
                self.i.easy(p_2._deck)
            else:
                self.i.hard(p_2._deck)

        # Start the game
        game.print_welcome_message()
        while not game.check_game_over():

            game.start_battle()
            game.print_stats()

            answer = input('press Enter to continue. Enter x to stop: ')
            if answer.lower() == 'x':
                break
            elif answer.lower() == 'restart':
                return self.do_Restart(self)
            elif mode.lower() == '1':
                if answer.lower() == 'cheat':
                    return self.do_Cheat(self)

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
