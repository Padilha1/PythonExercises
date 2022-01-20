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

class GeniusAI(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.avaiable_moves()) == 9:
            square = random.choice(game.avaiable_moves()) #random choose
        else:
            # get the square based off ALGORITHm
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter #yourself
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares()+ 1)
            }
        elif not state.empty_squares():
            return{'position': None, 'score': 0}

        #Initiate dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # cada score deve maximizar (be larger)
        else: 
            best = {'position': None, 'score': math.inf} #Descreasing 

        for possible_move in state.avaiable_moves():
            #1: make a move
            state.make_move(possible_move, player)
            #2: Using Minimax to SIMULATE a game after move
            sim_score = self.minimax(state, other_player) #alternate player

            #3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            #4: update dictionary if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
