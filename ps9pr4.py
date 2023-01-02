#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *


class AIPlayer(Player):

    def __init__(self, checker, tiebreak, lookahead):
        """Constructor function for AIPlayer class
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
        
    def __repr__(self):
        """ Print function for the AIPlayer class. Includes checker, tiebreaking strategy and lookahead value.
        """
        s = 'Player ' + self.checker + ' ' + '(' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s
    
    def max_score_column(self, scores):
        """Takes a list scores containing a score for each column of the board and returns the index of the column
        with the maximum score.
        """
        max_score = max(scores)
        max_list = []
        for x in range(len(scores)):
            if scores[x] == max_score:
                max_list += [x]
        if self.tiebreak == 'RIGHT':
            return max_list[-1]
        elif self.tiebreak == 'LEFT':
            return max_list[0]
        elif self.tiebreak == 'RANDOM':
            return random.choice(max_list)
    
    def scores_for(self, b):
        """Assesses the current board and returns a list of scores of either -1, 0, 50, 100, one value for each column,
        that will help determine the best next move for the AI Player.
        """
        scores = [0] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                new_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = new_player.scores_for(b)
                if max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                elif max(opp_scores) == 100:
                    scores[col] = 0
                b.remove_checker(col)
        return scores
    
    def next_move(self, b):
        """Returns the AIPlayer's judgement of the best possible next move.
        """
        scores = self.scores_for(b)
        return self.max_score_column(scores)
                
                

