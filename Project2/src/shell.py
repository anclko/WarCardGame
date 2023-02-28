import cmd
from game import WarCardGame
from deck import Deck
from Player import Player
from Intelligence import Intelligence


class Shell(cmd.Cmd):

    i = Intelligence()

    intro = "Type help or ? to list commands.\n"
    prompt = '> '
    
    def do_Start(self, _):
        '''Start The Game'''

        player1 = Player(input("Enter your name: "), Deck(is_empty=True))
        mode = input("Enter game mode 1 for PC, for 2nd Player: ")
        if mode == '2':
            player2 = Player(input("Enter opponent name: "), Deck(is_empty=True))
        else:
            player2 = Player("Computer", Deck(is_empty=True))
                
        # Create a new deck and game instance
        deck = Deck()
        game = WarCardGame(player1, player2, deck)

        if mode == '1':
            defficulty = input('what level do you want the PC to be easy/hard? ')
            if defficulty.lower() != 'easy' and defficulty.lower() != 'hard':
                defficulty = input('what level do you want the PC to be easy/hard? ')

            if defficulty.lower() == 'easy':
                self.i.easy(player2._deck)
            else:
                self.i.hard(player2._deck)


        # Start the game
        game.print_welcome_message()
        while not game.check_game_over():

            game.start_battle()
            game.print_stats()

            asnswer = input('press Enter to continue. Enter x to stop: ')
            if asnswer.lower() == 'x':
                break
            elif asnswer == 'restart':
                return self.do_restart(self)
            elif mode.lower() == '1':
                if asnswer.lower() == 'cheat':
                    return self.do_Cheat(self)

    def do_Exit(self, _):
        '''Exits the program'''
        print('Bye Bye!')
        return True
    
    def do_restart(self, _):
        '''Restarts The Game'''
        return self.do_Start(self)
    
    def do_Cheat(self, _):
        '''Win The Game By Cheating'''
        WarCardGame.cheat(self)
        
