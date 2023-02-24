import random
from card import Card
from suit import Suit


class Deck:

    SUITS = ("clubs", "diamonds", "hearts", "spades")

    def __init__(self, is_empty=False):
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit in Deck.SUITS:
            for value in range(2, 15):
                self._cards.append(Card(Suit(suit), value))

    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add(self, card):
        self._cards.insert(0, card)
