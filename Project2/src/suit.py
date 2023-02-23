class Suit:

    """Setting up the suit (symbol of card) class"""

    SYMBOLS = {"clubs": "♣", "diamonds": "♦", "hearts": "♥", "spades": "♠"}

    def __init___(self, description):
        # description : clubs,diamonds,hearts,spades
        self._description = description
        self._symbol = Suit.SYMBOLS[description.lower()]
    
    # ---- GETTER ---- #

    @property
    def description(self):
        return self._description

    @property
    def symbol(self):
        return self.symbol
