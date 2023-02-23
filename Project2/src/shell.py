import cmd
import Game

class Shell(cmd.Cmd):

    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = '(game) '
    
    def __init__(self):
        super().__init__()
        self.game = Game.Game()
    
    def do_Start(self,_):
        self.game.ask_game_mode()
    
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

    def do_Stats(self,_):
        self.game.print_stats()
    
if __name__ == "__main__":
    Shell().cmdloop()
