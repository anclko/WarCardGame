"""

========================
Welcome To The Card Game
========================

"""
from source.src import Shell


def main():
    """
    Runs the cmd loop to execute the program and also enables printing
    out doc strings.
    """
    print(__doc__)
    Shell.Shell().cmdloop()


if __name__ == "__main__":
    main()
