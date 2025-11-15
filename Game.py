
from Board import Board
from Player import Player

class Game:
    """board = Board()
    player = Player()
    computer = Player("O", False)"""


    def __init__(self):
        self.board = Board()
        self.player = Player()
        self.computer = Player("O", False)

    def start(self):
        self.board.print_board()
        
        while True:
            # Ask human user move
            move = self.player.get_player_move()
            # Submit move
            self.board.submit_move(move, self.player)
            # Print board
            self.board.print_board()

            if self.board.is_move_valid(move) and self.board.is_winner(self.player, move[0], move[1]):
                print("you win!")
                break

            # Ask computer player move
            comp_move = self.computer.get_player_move()
            # Submit move
            self.board.submit_move(comp_move, self.computer)
            # Print board
            self.board.print_board()

            if self.board.is_winner(self.computer, comp_move[0], comp_move[1]):
                print("The Computer won!")
                break

            comp_move = self.computer.get_computer_move()


# Ejecutar el juego
if __name__ == "__main__":
    game = Game()
    game.start()
