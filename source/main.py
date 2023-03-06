"""
Class that consists of the command to run the game.
"""
from source.src import shell


def main():
    """ 
    Runs the cmd loop to execute the program and also enables printing
    out doc strings.
    """
    print(__doc__)
    shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
