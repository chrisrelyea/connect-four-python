# connect-four-python

Connect four game with several different AI player difficulty levels. Created as coursework for Boston University's CS111 course in Fall 2021.




----FILE INFO----

Four files are included:


ps9pr1.py
  Defines the Board class - creates a functional connect four board to be played in the console. Includes functions to check if a checker can be added to a given column, if there are any rows of four on the board, etc.
  
  
ps9pr2.py
  Defines the Player class - creates a human player such that when run, the connect_four function will ask for inputs from the user. Can be either 'X' or 'O' checkers.
  
  
  
ps9pr3.py
  Defines the connect_four function - when run, this function plays a game of Connect Four with the two included fields (filled by Player or AIPlayer objects).
  NOTE: In the connect_four function, Board b is created as a 6x7 board. The dimensions of the board can be changed from these hardcoded values and the game still functions as normal.
  Also defined in this file is the RandomPlayer class, a type of AI Player that makes completely random moves.
  
  
  
ps9pr4.py
  Defines the AIPlayer class. An AIPlayer object has four init fields:
  
  Checker - assigns 'X' or 'O' as the player's checker
    
  Tiebreak - if the AIPlayer decides that multiple moves are in its best interest, the tiebreak value, "LEFT" or "RIGHT" tells the AI to choose the leftmost best move or the rightmost best move,                 respectively. The value can also be "RANDOM" to choose a random best move.
    
 Lookahead - determines the amount of moves the AI can "see into the future." Using recursion, the AI        will assess the outcome of every possible move it could make as well as a certain amount of moves on        top of that move using the resulting hypothetical board. The amount of future possible moves the AI is      assessing is the lookahead value. 
    
    
    
----HOW TO USE----

Once all four files are run and recognized by the IDE, the connect_four function must be run in the console. First, create Player or AIPlayer objects to be used in the game. Example:

p1 = Player('X')
p2 = AIPlayer('O', 'LEFT', 2)

We have created one player object for user input, and an AIPlayer object for the user to play against. Valid games can be played between two AIPlayerss, two Players, or an AIPlayer and a Player. 

Next, simply run the connect_four function with the created objects.

connect_four(p1,p2)

The game will then proceed in the console until a winner is determined.

Good luck!


--Christopher Relyea
    
  
  
