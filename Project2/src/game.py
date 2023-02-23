class Game:

    PLAYER1 = 0
    PLAYER2 = 1
    TIE = 2

    def __init__(self, player, player2, deck):
        pass

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

    def welcome_message(self):
        pass
