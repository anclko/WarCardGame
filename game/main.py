"""

========================
Welcome To The Card Game
========================

"""
from game.shell import Shell


def main():
    """Run the game by starting the command-line interface.

    This function starts the game by printing a brief description of the game,
    and then launching a command-line interface that allows the player to
    interact with the game. The game continues until the player chooses to quit
    the game or until the game ends.

    Returns:
    None
    """
    print(__doc__)
    Shell().cmdloop()


if __name__ == "__main__":
    main()
