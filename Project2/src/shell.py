import cmd
import game


class Shell(cmd.Cmd):
    """Example of class with command actions to roll a dice."""

    intro = "Welcome to the War Game! Type help or ? to list commands.\n"
    prompt = "(game) "

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = game.Game()

    def do_start(self, _):
        """Start the game with a new number."""
        msg = (
            "I am ready and is now thinking of a new secret number"
            " between {} and {}."
        )
        self.game.start()
        print(msg.format(self.game.low(), self.game.high()))

    def do_cheat(self, _):
        """Cheat to view the secret number."""
        print("Cheater... the number is {}.".format(self.game.cheat()))

    def do_guess(self, arg):
        """Do a guess of a number."""
        msg = "Missing argument on the number you are guessing. Try 'guess 42"
        if not arg:
            print(msg)
            return

        a_number = int(arg)
        try:
            print("Your'e guess is -> {}".format(self.game.guess(a_number)))
        except ValueError as error:
            print(error)

    def do_exit(self, _):
        # pylint: disable=no-self-use
        """Leave the game."""
        print("Bye bye - see ya soon again")
        return True

    def do_quit(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_quitty(self, arg):
        """Leave the game."""
        return self.do_exit(arg)

    def do_EOF(self, arg):
        # pylint: disable=invalid-name
        """Leave the game."""
        return self.do_exit(arg)
