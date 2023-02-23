class Game:

    PLAYER1 = 0
    PLAYER2 = 1
    TIE = 2

    def __init__(self, player1, player2, deck):
        self._deck = deck
        self._player1 = None
        self._player2 = None
        self._game_mode = None
        self._make_initial_deck()

    def ask_game_mode(self):
        while self._game_mode not in ["1", "2"]:
            self._game_mode = input("One (1) or Two (2) players?")

    def make_initial_deck(self):
        pass

    def make_deck(self, thisPlayer):
        pass

    def battle(self, WarCards=None):
        pass

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
