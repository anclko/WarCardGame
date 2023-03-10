"""Class Deck"""
from game.card import Card
from game.suit import Suit
import random
import sys
sys.stdout.reconfigure(encoding='utf-8')


class Deck:
    """A class representing a deck of playing cards.

    Attributes:
    SUITS (tuple): A tuple of strings representing the
    four suits in a deck of cards.

    Methods:
    __init__(self, is_empty=False): Initializes a new instance
    of the Deck class.
    build(self): Builds a standard deck of 52 cards.
    size(self): Returns the number of cards in the deck.
    show(self): Prints each card in the deck.
    shuffle(self): Shuffles the cards in the deck.
    draw(self): Removes and returns the top card from the deck.
    add(self, card): Adds a card to the bottom of the deck.
    """

    SUITS = ("clubs", "diamonds", "hearts", "spades")

    def __init__(self, is_empty=False):
        """Initialize a new instance of the Deck class.

        Args:
        is_empty (bool, optional): Whether to create an empty deck.
        Defaults to False.
        """
        self._cards = []

        if not is_empty:
            self.build()

    @property
    def size(self):
        """Return the number of cards in the deck."""
        return len(self._cards)

    def build(self):
        """Build a standard deck of 52 cards."""
        for suit in Deck.SUITS:
            for value in range(2, 15):
                self._cards.append(Card(Suit(suit), value))

    def show(self):
        """Print out the details of each card in the deck."""
        for card in self._cards:
            card.show()

    def shuffle(self):
        """Randomly shuffles the order of the cards in the deck."""
        random.shuffle(self._cards)

    def draw(self):
        """Remove and gives the top card of deck. None if the deck is empty."""
        if self._cards:
            return self._cards.pop()
        else:
            return None

    def add(self, card):
        """Add the given card to the bottom of the deck.."""
        self._cards.insert(0, card)
