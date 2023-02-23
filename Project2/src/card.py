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
