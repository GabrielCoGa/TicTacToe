from operator import truediv


class Board:
    EMPTY = 0
    COLUMNS = {"A": 0, "B": 1, "C": 2}
    ROWS = (1, 2, 3)

    def __init__(self, game_board=None):
        if game_board:
            self.game_board = game_board
        else:
            self.game_board = [[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]]

    def print_board(self):
        print("     A   B   C")
        for i, row in enumerate(self.game_board, 1):
            print(i, end=" | ")
            for col in row:
                if col != Board.EMPTY:
                    print(col, end=" | ")
                else:
                    print(" ", end=" | ")
            print("\n---------------")

    def submit_move(self, move, player):
        if not self.is_move_valid(move):
            print("Invalid Input: Please Enter the row and columns of your move (Example: 1A)")
            return
        else:
            row_index = int(move[0]) - 1
            col_index = Board.COLUMNS[move[1]]
            value = self.game_board[row_index][col_index]

            if value == Board.EMPTY:
                self.game_board[row_index][col_index] = player.marker
            else:
                print("This space is already taken")

    def is_move_valid(self, move):  #1A
        return ((len(move) == 2)
            and (int(move[0] in Board.ROWS))
            and (move[1] in Board.COLUMNS))

    def is_winner(self, player, row, col):
        if self.check_row(row, player):
            return  True
        elif self.check_col(col, player):
            return True
        elif self.check_diagonal(player):
            return True
        elif self.check_antidiagonal(player):
            return True
        else:
            return False

    def check_row(self, row, player):
        row_index = int(row) - 1
        board_row = self.game_board[row_index]

        if board_row.count(player.marker) == 3:
            return True
        else:
            return False

    def check_col(self, col, player):
        col_index = Board.COLUMNS[col]
        total_markers = 0

        for i in range(3):
            if self.game_board[1][col_index] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return  False

    def check_diagonal(self, player):
        total_markers = 0

        for i in range(3):
            if self.game_board[i][i] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return  True
        else:
            return False

    def check_antidiagonal(self, player):
        total_markers = 0

        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                total_markers += 1

        if total_markers == 3:
            return True
        else:
            return False

