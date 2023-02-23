class Card:

    """ Creating Card class - Special cards and regular cards"""

    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    # ----- GETTER ---- #

    @property
    def suit(self):
        return self._suit

    @property
    def value(self):
        return self._value

    # ---- CARD ACTIONS ---- #

    def show(self):
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol

        # condition if card is "special" then print the name of card
        # suit and symbol. For other card, just their value suit and symbol
