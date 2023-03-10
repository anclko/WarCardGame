"""Doc."""


class Suit:
    """Doc."""

    SYMBOLS = {"clubs": "♣", "diamonds": "♦", "hearts": "♥", "spades": "♠"}

    def __init__(self, description):
        """Doc."""
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]

    @property
    def description(self):
        """Doc."""
        return self._description

    @property
    def symbol(self):
        """Doc."""
        return self._symbol
