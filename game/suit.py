"""Class Suit."""


class Suit:
    """Attributes:.

    SYMBOLS (dict): A dictionary mapping suit descriptions to their symbols.

    Methods:
    __init__(description): Suit object with the given description and symbol.
    description(): Returns the description of the suit.
    symbol(): Returns the symbol of the suit.
    """

    SYMBOLS = {"clubs": "♣", "diamonds": "♦", "hearts": "♥", "spades": "♠"}

    def __init__(self, description):
        """Construct a Suit object with the given description and symbol.

        Args:
        description (str): The description of the suit.

        Returns:
        A Suit object with the given description and corresponding symbol.
        """
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]

    @property
    def description(self):
        """Returns the description of the suit.

        Args:
        None

        Returns:
        The description of the suit as a string.
        """
        return self._description

    @property
    def symbol(self):
        """Returns the symbol of the suit.

        Args:
        None

        Returns:
        The symbol of the suit as a string.
        """
        return self._symbol
