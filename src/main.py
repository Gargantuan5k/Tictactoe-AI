import math
import time
import os
import sys
from players import HumanPlayer, RandomPlayer, AIPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None
    
    @staticmethod
    def make_board():
        return [" " for _ in range(9)]
    
    def print_board(self):
        os.system("clear")
        
        for row in [self.board[i*3: (i+1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        # print hint for square numbers 0 | 1 | 2 ...
        number_board = [[str(i) for i in range(j*3, (j+1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")
    
    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False
    
    def winner(self, square, letter):
        # Check rows
        row_idx = math.floor(square / 3)
        row = self.board[row_idx * 3:(row_idx+1)*3]
        if all([s == letter for s in row]):
            return True
        
        col_idx = square % 3
        column = [self.board[col_idx+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        
        return False


    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums
    
    letter = "X"
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")
            
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter
            
            letter = "O" if letter == "X" else "X"
        
        time.sleep(0.8)
    
    if print_game:
        print("It's a tie!")


def run():
    print("WELCOME TO TIC-TAC-TOE!")
    print("X------------------------------------------------------------------------------------------------X")
    print("You can choose player 1 or player 2. They can be Human(H), Random Computer Moves (R) or AI (AI). Player 1 uses the X token "
        "and player 2 uses O. Both players are Human by default.")
    print("The Human Player is controlled by you. The AI is unbeatable and chooses its own moves. Random chooses any move on the board"
        " at random.")
    print("X------------------------------------------------------------------------------------------------X")

    p1 = input("Choose Player 1 (H/AI/R): ").strip().lower()
    p2 = input("Choose Player 2 (H/AI/R): ").strip().lower()

    if p1 == "ai":
        x_player = AIPlayer("X")
    elif p1 == "h":
        x_player = HumanPlayer("X")
    elif p1 == "r":
        x_player = RandomPlayer("X")
    else:
        x_player = HumanPlayer("X")

    if p2 == "ai":
        o_player = AIPlayer("O")
    elif p2 == "h":
        o_player = HumanPlayer("O")
    elif p2 == "r":
        o_player = RandomPlayer("O")
    else:
        o_player = HumanPlayer("O")
    
    print("X------------------------------------------------------------------------------------------------X\n")

    print(f"Player 1 (X) is {p1}")
    print(f"Player 2 (O) is {p2}")

    ctd = 5
    while ctd:
        try:
            sys.stdout.write(f"\rStarting in {ctd}...")
            sys.stdout.flush()
            time.sleep(1)
            ctd -= 1
        except KeyboardInterrupt:
            break
    
    print("\n")
    game = TicTacToe()

    os.system("clear")
    play(game, x_player, o_player, print_game=True)


if __name__ == "__main__":
    while True:
        pg = input("Play? (y/n)").strip().lower()
        if pg == "y":
            os.system("clear")
            run()
        else:
            break
