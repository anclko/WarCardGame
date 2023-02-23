import cmd
import Game

class Shell(cmd.Cmd):

    intro = "Welcome to the game. Type help or ? to list commands.\n"
    prompt = '(game) '
    
    def __init__(self,game):
        super().__init__()
        self.game = game.Game()
    
    def do_Start(self):
        pass
    
    def do_Exit(self,line):
        '''Exits the program'''
        print('Bye Bye!')
        return True
    
    def do_restart(self,line):
        '''Restarts The Game'''
        return self.do_Start()
    
    def do_Cheat():
        '''Win The Game By Cheating'''
        pass

    def do_ChangeName():
        '''Change your Name'''
        pass
    
if __name__ == "__main__":
    Shell().cmdloop()
