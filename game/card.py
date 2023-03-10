"""Doc."""
import sys

sys.stdout.reconfigure(encoding="utf-8")


class Card:
    """Doc."""

    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        """Doc."""
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        """Doc."""
        return self._suit

    @property
    def value(self):
        """Doc."""
        return self._value

    def show(self):
        """Doc."""
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")

    def is_special(self):
        """Doc."""
        return self._value >= 11

    def __lt__(self, other_card):
        """Doc."""
        if self.value < other_card._value:
            return True
        else:
            return False

    def __gt__(self, other_card):
        """Doc."""
        if self._value > other_card._value:
            return True
        else:
            return False
