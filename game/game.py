"""Game Logic."""


class WarCardGame:
    """
    A class representing a game of War Card.

    Attributes:
    PLAYER: int
        A constant representing the first player.
    PLAYER2: int
        A constant representing the second player.
    TIE: int
        A constant representing a tie between players.

    Methods:
    __init__(self, player, player2, deck)
        Initializes a WarCardGame object with the given players and deck.
    make_initial_decks(self)
        Distributes the cards in the deck to the players at the
        start of the game.
    make_deck(self, character)
        Adds 26 cards to the given player's deck.
    start_battle(self, war_cards=None)
        Initiates a round of the game, displaying each player's card and
        determining the winner.
    get_round_winner(self, player_card, player2_card)
        Determines the winner of a round based on the two cards played.
    get_cards_won(self, player_card, player2_card, previous_cards)
        Returns a list of the cards won by the winning player of a round.
    add_cards_to_players(self, character, list_of_cards)
        Adds a list of cards to a player's deck.
    start_war(self, battle_cards)
        Initiates a war between the players, with the given cards
        played as the stakes.
    check_game_over(self)
        Determines if the game is over by checking if either player
        has an empty deck.
    print_stats(self)
        Prints the current number of cards in each player's deck.
    print_welcome_message(self)
        Prints a welcome message for the start of the game.
    cheat(self)
        Ends the game and declares the player the winner for cheating.
    """

    PLAYER = 0
    PLAYER2 = 1
    TIE = 2

    def __init__(self, player, player2, deck):
        """Initialize a new game of War Card.

        Args:
        player (Player): The first player.
        player2 (Player): The second player.
        deck (Deck): The deck of cards to be used in the game.
        """
        self._player = player
        self._player2 = player2
        self._deck = deck
        self.make_initial_decks()

    def make_initial_decks(self):
        """Shuffle the deck and deal half of the cards to each player."""
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._player2)

    def make_deck(self, character):
        """Deal 26 cards to the given player.

        Args:
        character (Player): The player to deal cards to.
        """
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, war_cards=None):
        """Start a new round of the game.

        Args:
            war_cards (list of Card objects, optional): A list of cards played
                in a previous tie. Defaults to None.

        Returns:
            int: The winner of the round, as an integer:
                * WarCardGame.PLAYER if the player wins
                * WarCardGame.PLAYER2 if the player2 wins
                * WarCardGame.TIE if it's a tie.

        Raises:
            ValueError: If the war_cards argument is provided but it's not a
                list of Card objects.

        Prints:
            A message to the console displaying the cards played by
            each player,
            the winner of the round and the number of cards won.

        This method draws one card from each player's deck and compares them to
        determine the winner of the round. If there's a tie, a war occurs and
        the start_war method is called. The cards won are added to the winner's
        deck, and the winner of the round is returned as an integer.
        The winner of the round.
        """
        print("==============================")
        print("|   Let's Start The Battle   |")
        print("==============================")

        player_card = self._player.draw_card()
        player2_card = self._player2.draw_card()

        print(f"{self._player.name}'s card:")
        player_card.show()

        print(f"\n{self._player2.name}'s card: ")
        player2_card.show()

        winner = self.get_round_winner(player_card, player2_card)
        cards_won = self.get_cards_won(player_card, player2_card, war_cards)

        if winner == WarCardGame.PLAYER:
            print(f"\n{self._player.name} won this round!")
            self.add_cards_to_players(self._player, cards_won)
        elif winner == WarCardGame.PLAYER2:
            print(f"\n{self._player2.name} won this round.")
            self.add_cards_to_players(self._player2, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)

        return winner

    def get_round_winner(self, player_card, player2_card):
        """Determine the winner of a round.

        Args:
        player_card (Card): The card played by the first player.
        player2_card (Card): The card played by the second player.

        Returns:
        int: The winner of the round.
        """
        if player_card.value > player2_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < player2_card.value:
            return WarCardGame.PLAYER2
        else:
            return WarCardGame.TIE

    def get_cards_won(self, player_card, player2_card, previous_cards):
        """Get the cards won by the winner of a round.

        Args:
        player_card (Card): The card played by the first player.
        player2_card (Card): The card played by the second player.
        previous_cards (list): A list of cards played in a previous tie.

        Returns:
        list: The cards won by the winner of the round.
        """
        if previous_cards:
            return [player_card, player2_card] + previous_cards
        else:
            return [player_card, player2_card]

    def add_cards_to_players(self, character, list_of_cards):
        """Add a list of cards to a player's deck.

        Args:
        character (Player): The player to add cards to.
        list_of_cards (list): The list of cards to add.
        """
        for card in list_of_cards:
            character.add_card(card)

    def start_war(self, battle_cards):
        """
        Start a war round.

        Args:
        battle_cards (list): The list of cards that triggered the war.
        """
        player_cards = []
        player2_cards = []

        for i in range(1):
            player_card = self._player.draw_card()
            player_cards.append(player_card)

            player2_card = self._player2.draw_card()
            player2_cards.append(player2_card)

        print("Two hidden cards: X X")

        self.start_battle(player_cards + player2_cards + battle_cards)

    def check_game_over(self):
        """
        Check if the game is over.

        Returns:
        bool: True if the game is over, False otherwise.
        """
        if self._player.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print(f"{self._player2.name} won! Congratulations.")
            return True
        elif self._player2.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print(f"{self._player.name} won! Congratulations.")
            return True
        else:
            return False

    def print_stats(self):
        """Print the current number of cards each player has."""
        print("\n----")
        print(f"{self._player.name} has {self._player.deck.size} cards.")
        print(f"{self._player2.name} has {self._player2.deck.size} cards.")
        print("----")

    def print_welcome_message(self):
        """Print the welcome message for the game."""
        print("==============================")
        print("|        War Card Game       |")
        print("==============================")

    def cheat(self):
        """Tells that the player has cheated & won the game."""
        print("===========================")
        print("|        Game Over        |")
        print("===========================")
        print("You Won By Cheating!.")
