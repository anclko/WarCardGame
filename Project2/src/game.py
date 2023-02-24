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

        winner = self.get_round_winner(player_card, player2_card)
        cards_won = self.get_cards_won(player_card, player2_card, warCards)

        if winner == WarCardGame.PLAYER:
            print("\nYou won this round!")
            self.add_cards_to_players(self._player, cards_won)
        elif winner == WarCardGame.PLAYER2:
            print("\nPlayer 2 won this round.")
            self.add_cards_to_players(self._player2, cards_won)
        else:
            print("\nIt's a tie. This is war!")
            self.start_war(cards_won)

        return winner
        
    def get_round_winner(self, player1_card, player2_card):
        pass

    def get_cards_won(self, player_card, computer_card, previous_cards):
        pass

    def add_cards_to_players(self, thisPlayer, list_of_cards):
        for card in list_of_cards:
            thisPlayer.add_card(card)

    def start_war(self, battleCards):
        player_cards = []
        player2_cards = []

        for i in range(3):
            player_card = self._player.draw_card()
            player_cards.append(player_card)

            player2_card = self._player2.draw_card()
            player2_cards.append(player2_card)

        print("Six hidden cards placed: XXX XXX")

        self.start_battle(player_cards + player2_cards + battleCards)

    def game_over(self):
        if self._player.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print("Try again. Player 2 won.")
            return True
        elif self._player2.has_empty_deck():
            print("===========================")
            print("|        Game Over        |")
            print("===========================")
            print(f"Congratulations! You won, {self._player.name}! Congratulations.")
            return True
        else:
            return False

    def print_stats(self):
        print("\n----")
        print(f"You have {self._player.deck.size} cards on your deck.")
        print(f"Player 2 has {self._player2.deck.size} cards on its deck.")
        print("----")

    def print_welcome_message(self):
        print("♣----------------------------♦")
        print("|        War Card Game       |")
        print("♥----------------------------♠")
