"""Doc."""
import random
from game.card import Card
from game.suit import Suit
import sys

sys.stdout.reconfigure(encoding="utf-8")


class Deck:
    """Doc."""

    SUITS = ("clubs", "diamonds", "hearts", "spades")

    def __init__(self, is_empty=False):
        """Doc."""
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        """Doc."""
        return len(self._cards)

    def build(self):
        """Doc."""
        for suit in Deck.SUITS:
            for value in range(2, 15):
                self._cards.append(Card(Suit(suit), value))

    def show(self):
        """Doc."""
        for card in self._cards:
            card.show()

    def shuffle(self):
        """Doc."""
        random.shuffle(self._cards)

    def draw(self):
        """Doc."""
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add(self, card):
        """Doc."""
        self._cards.insert(0, card)
