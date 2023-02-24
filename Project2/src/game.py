class WarCardGame:

    PLAYER = 0
    PLAYER2 = 1
    TIE = 2

    def __init__(self, player, player2, deck):
        self._player = player
        self._player2 = player2
        self._deck = deck
        self.make_initial_decks()

    def make_initial_decks(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._player2)

    def make_deck(self, thisPlayer):
        for i in range(26):
            card = self._deck.draw()
            thisPlayer.add_card(card)

    def start_battle(self, warCards=None):

        print("==============================")
        print("|   Let's Start The Battle    |")
        print("==============================")

        player_card = self._player.draw_card()
        player2_card = self._player2.draw_card()

        print("Your Card:")
        player_card.show()

        print("\nPlayer 2 Card: ")
        player2_card.show()
        
    def get_round_winner(self, player1_card, player2_card):
        pass

    def get_cards_won(self, player_card, computer_card, previous_cards):
        pass

    def add_cards_to_thisPlayer(self, thisPlayer, list_of_cards):
        pass

    def war(self, battleCards):
        pass

    def game_over(self):
        pass

    def print_stats(self):
        pass

    def print_welcome_message(self):
        print("♣----------------------------♦")
        print("|        War Card Game       |")
        print("♥----------------------------♠")
