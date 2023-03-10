"""Class Player."""


class Player:
    """
    A class representing a player in the card game.

    Attributes:
    None

    Methods:
    __init__(name, deck): Constructs a Player object with the
    given name and deck.
    deck(): Returns the player's deck.
    has_empty_deck(): Returns True if the player's deck is empty,
    False otherwise.
    has_less_than_4_cards(): Returns True if the player's deck has
    less than 4 cards, False otherwise.
    draw_card(): Draws a card from the player's deck and returns it.
    add_card(card): Adds a card to the player's deck.
    """

    def __init__(self, name, deck):
        """Construct a Player object with the given name and deck.

        Args:
        name (str): The name of the player.
        deck (Deck): The deck of cards for the player.

        Returns:
        A Player object with the given name and deck.
        """
        self.name = name
        self._deck = deck

    @property
    def deck(self):
        """Returns the player's deck.

        Args:
        None

        Returns:
        The player's deck as a Deck object.
        """
        return self._deck

    def has_empty_deck(self):
        """Return True if the player's deck is empty, False otherwise.

        Args:
        None

        Returns:
        True if the player's deck is empty, False otherwise.
        """
        return self._deck.size == 0

    def draw_card(self):
        """Return: The card drawn from the deck, None if the deck is empty."""
        if not self.has_empty_deck():
            return self._deck.draw()
        else:
            return None

    def add_card(self, card):
        """Add a card to the deck.

        Args:
        card: A Card object to be added to the deck.
        """
        self._deck.add(card)
