#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###

    def __init__(self, height, width):
        """constructor for Board object
        """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
        s += 2 * self.width * '-' + '-'
        s += '\n'
        for col in range(self.width):
            if col > 9:
                s += ' ' + str(col%10)
            else:
                s += ' ' + str(col)
 
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row = 0
        while row < self.height and self.slots[row][col] == ' ':
            row += 1

        self.slots[row-1][col] = checker
                
        

    
    
        
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    
                
    def reset(self):
        """clears the current board to represent an empty board
        """
        self.slots = Board(self.height, self.width).slots
        
    
    def can_add_to(self, col):
        """returns True if adding a checker to column is a valid move, i.e.
        the column exists on the board and is not full. False otherwise.
        """
        if col in range(0, self.width) and self.slots[0][col] == ' ':
            return True
        else:
            return False
        
    def is_full(self):
        """returns True if the board object is completely full, and false
        otherwise.
        """
        for col in range(self.width):
            if self.can_add_to(col) == True:
                return False
        return True

    def remove_checker(self, col):
        """removes the topmost checker from the specified column. Does nothing
        if the column is empty
        """
        done = False
        row = 0
        while row < self.height and done == False:
            if self.slots[row][col] == ' ':
                row += 1
            else:
                self.slots[row][col] = ' '
                done = True
    
    def is_win_for(self, checker):
        """ Tests if the board contains a four in a row for the given checker
        """
        
        assert(checker == 'X' or checker == 'O')
        
        if self.is_horizontal_win(checker) == True or \
            self.is_vertical_win(checker) == True or \
                self.is_down_diagonal_win(checker) == True or \
                    self.is_up_diagonal_win(checker):
                        return True
        else:
            return False
        
        
    def is_horizontal_win(self, checker):
        """ Tests if the board contains a horizontal line of four of the given checkers
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                        self.slots[row][col + 2] == checker and \
                            self.slots[row][col + 3] == checker:
                                return True

        return False
    
    def is_vertical_win(self, checker):
        """Tests if the board contains a vertical line of four of the given checker
        """
        for col in range(self.width):
            for row in range(self.height-3):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                        self.slots[row + 2][col] == checker and \
                            self.slots[row+3][col] == checker:
                                return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """ Tests if the board contains a win of the given checker in the down diagonal 
        orientation
        """
        
        for col in range(self.width-3):
            for row in range(self.height-3):
                if self.slots[row][col] == checker and \
                    self.slots[row+1][col+1] == checker and \
                        self.slots[row+2][col+2] == checker and \
                            self.slots[row+3][col+3] == checker:
                                return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """Tests if the board contains a win of the given checker in the up diagonal
        orientation
        """
        for col in range(self.width-3):
            for row in range(3, self.height):
                if self.slots[row][col] == checker and \
                    self.slots[row-1][col+1] == checker and \
                        self.slots[row-2][col+2] == checker and \
                            self.slots[row-3][col+3] == checker:
                                return True
        return False
    
    
    

    
                    
                    
            
    
