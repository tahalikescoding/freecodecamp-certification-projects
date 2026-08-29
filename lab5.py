"""
PLAYER INTERFACE
"""


from abc import ABC , abstractmethod
import random

class Player(ABC):
    def __init__(self)->None:
        self.moves = []
        self.position = (0,0)
        self.path = [self.position]

    def make_move(self)->tuple:
        move = random.choice(self.moves)
        new_position =tuple(sum(tup) for tup in list(zip(move , self.position)))
        self.position = new_position
        self.path.append(new_position)
        return new_position
    
    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(0,1) , (0,-1) , (1,0) , (-1,0)] 
    def level_up(self):
        self.moves.extend([(1,1) , (-1,-1), (1,-1), (-1,1)])


