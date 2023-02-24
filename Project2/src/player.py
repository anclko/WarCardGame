class Player:

    def __init__(self, name, deck, is_player2=False):
        self.name = name
        self._deck = deck
        self._is_player2 = is_player2

    @property
    def is_player2(self):
        return self._is_player2

    @property
    def deck(self):
        return self._deck

    def has_empty_deck(self):
        return self._deck.size == 0

    def draw_card(self):
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        self._deck.add(card)
