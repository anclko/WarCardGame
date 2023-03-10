"""Class Card."""
import sys
sys.stdout.reconfigure(encoding='utf-8')


class Card:
    """Class representing a standard playing card."""

    SPECIAL_CARDS = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

    def __init__(self, suit, value):
        """Initialize a Card object with a specified suit and value.

        Parameters:
        suit (Suit): The suit of the card.
        value (int): The value of the card, between 2 and 14.

        Returns:
        None
        """
        self._suit = suit
        self._value = value

    @property
    def suit(self):
        """Returns the suit of the card.

        Parameters:
        None

        Returns:
        Suit: The suit of the card.
        """
        return self._suit

    @property
    def value(self):
        """Returns the value of the card.

        Parameters:
        None

        Returns:
        int: The value of the card.
        """
        return self._value

    def show(self):
        """Print the card's value, suit, and symbol to the console.

        Parameters:
        None

        Returns:
        Non
        """
        card_value = self._value
        card_suit = self._suit.description.capitalize()
        suit_symbol = self._suit.symbol

        if self.is_special():
            card_description = Card.SPECIAL_CARDS[card_value]
            print(f"{card_description} of {card_suit} {suit_symbol}")
        else:
            print(f"{card_value} of {card_suit} {suit_symbol}")

    def is_special(self):
        """Return True if the card is a special card, False otherwise.

        Parameters:
        None

        Returns:
        bool: True if the card is a special card, False otherwise.
        """
        return self._value >= 11

    def __lt__(self, other_card):
        """Override the < operator to compare two Card based on their values.

        Parameters:
        other_card (Card): The other Card object to compare to.

        Returns:
        bool: True if the value of Card is less than the value
        of the other Card, False otherwise.
        """
        if self.value < other_card._value:
            return True
        else:
            return False

    def __gt__(self, other_card):
        """Override the > operator to compare two Card objects based on values.

        Parameters:
        other_card (Card): The other Card object to compare to.

        Returns:
        bool: True if the value of this Card is greater than the
        value of the other Card, False otherwise.
        """
        if self._value > other_card._value:
            return True
        else:
            return False
