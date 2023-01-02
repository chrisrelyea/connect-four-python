#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board


class Player:
    """ A data type to represent a player in the connect four game
    """
    
    def __init__(self, checker):
        """ Constructor function for Player class
        """
        
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ Print function for Player class, returns string
        indicating which checker the player is using.
        """
        
        s = 'Player ' + self.checker

        return s
    
    def opponent_checker(self):
        """ Returns the checker that the opponent is using in a 
        single character string X or O
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """ Gets the next move from the player, returns column number
        """
        
        choice = int(input('Enter a column: '))
        while b.can_add_to(choice) == False:
            print('Try again!')
            print()
            choice = int(input('Enter a column: '))
        self.num_moves += 1
        return choice
                
        
    
    
