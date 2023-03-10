"""Doc."""


class Player:
    """Doc."""

    def __init__(self, name, deck):
        """Doc."""
        self.name = name
        self._deck = deck
        self.in_war = False

    @property
    def deck(self):
        """Doc."""
        return self._deck

    def has_empty_deck(self):
        """Doc."""
        return self._deck.size == 0

    def draw_card(self):
        """Doc."""
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        """Doc."""
        self._deck.add(card)
