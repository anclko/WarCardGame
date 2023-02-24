import cmd
from Game import WarCardGame
from deck import Deck

class Shell(cmd.Cmd):


    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = '(game) '
    
    
    def do_Start(self,_):
        '''Start The Game'''

        player1 = input("Enter your name: ")
        mode = input("Enter game mode (computer/human): ")
        if mode.lower() == "human":
            player2 = input("Enter opponent name: ")
        else:
            player2 = "Computer"

        # Create a new deck and game instance
        deck = Deck()
        game = WarCardGame(player1, player2, deck)

        # Start the game
        game.print_welcome_message()
        while not game.check_game_over():
            game.print_stats()
            game.start_battle()
        

    def do_Exit(self,_):
        '''Exits the program'''
        print('Bye Bye!')
        return True
    
    def do_restart(self,_):
        '''Restarts The Game'''
        return self.do_Start(self)
    
    def do_Cheat(self,_):
        '''Win The Game By Cheating'''
        pass

    def do_ChangeName(self,_):
        '''Change your Name'''
        pass

    
