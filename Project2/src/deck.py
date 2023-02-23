import random
from card import Card
from suit import Suit

class Deck:
    """ Build the card deck """
    SUITS = ("Club", "Diamonds", "Hearts", "Spades")

    def __init__(self, is_empty=False):
        # Creating empty deck of card
        self._cards = []

        # Start with empty deck, if deck empty, build deck
        if not is_empty:
            self.build()

    # ---- GETTER ---- #
