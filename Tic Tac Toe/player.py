import math
from multiprocessing.sharedctypes import Value
import random 


class Player:
    def __init__(self, letter) :
        #letter is x or o
        self.letter = letter

    #all players get ther next move
    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        # random valid spot for next move
        square = random.choice(game.avaiable_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\s turn. Put move (0-8): ')

            try:
                val= int(square)
                if val not in game.avaiable_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try again')
                
        return val