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
    @property
    def size(self):
        return len(self._cards)

    # ---- DECK ACTIONS ---- #
    """ Building a deck, with a card of each value in its suit """
    def build(self):
        for suit in Deck.SUITS:
            for value in range(2, 15):
                self._cards.append(Card(Suit(suit), value))

    """ Show the card from deck """
    def show(self):
        for card in self._cards:
            card.show()

    """ adding random cards into the deck """
    def shuffle(self):
        random.shuffle(self._cards)

    """ Drawing a card from deck to play """
    def draw(self):
        if self._cards:
            # drawing card from top of deck, so has to be from
            # end of the list - pop()
            return self._cards.pop()
        else:
            return None

    """ Add cards to the beginning of deck for cards won """
    def add(self, card):
        self._cards.insert(0, card)
