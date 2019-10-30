import itertools

class TaTeTi():

    def __init__(self, initialBoard = None):
        if not initialBoard:
            self.board = [' ' for _ in range(9)]
        else:
            self.board = initialBoard

    def win(self):
        rows = [[self.board[0],self.board[1], self.board[2]], [self.board[3], self.board[4], self.board[5]], [self.board[6], self.board[7], self.board[8]]]

        diagonals = [ [self.board[0], self.board[4], self.board[8]], [self.board[2], self.board[4], self.board[6]] ]

        columns = [[self.board[0],self.board[3], self.board[6]], [self.board[1], self.board[4], self.board[7]], [self.board[2], self.board[5], self.board[8]]]

        lines = rows + columns + diagonals

        for line in lines:
            if (all(board_position == 'x' for board_position in line) or
            all(board_position == 'o' for board_position in line)):
                return True
        
    def full(self):
        if self.board.count(' ') > 0:
            return False
        
        else:
            return True


    def validate(self, position):
        return self.board[position-1] == " "

    def assign(self, position, piece):
        if self.validate(position):
            self.board[position-1] = piece
        else:
            raise Exception

    def draw_board(self):
        self.display = '\n'
        for i in range(9):
            if self.board[i] != ' ':
                self.display += ' ' + self.board[i] + ' '
            else:
                self.display += ' ' + str(1+i) + ' '
            if i == 2 or i == 5:
                self.display += '\n---+---+---\n'
            elif i == 8:
                self.display += '\n'
            else:
                self.display += '|'

        return self.display