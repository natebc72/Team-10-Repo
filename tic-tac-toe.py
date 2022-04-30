# tic-tac-toe 
# Author Jason Harrison


from re import S


def main():
   board = create_board
   player = next_player("")
   while not (we_have_a_winner(board) or its_a_tie(board)):
      draw_board(board)
      your_move(player, board)
      player = next_player(player)
   draw_board(board)
   print("Good game, thanks for playing")


def create_board():
   board = []
   for square in range(9):
       board.append(square + 1)
   return board 

def next_player(current_player):
   if current_player == "" or current_player == "o":
      return "x"
   elif current_player == "x":
      return "o"

def draw_board(board):
   print()
   print(f"{board[0]}|{board[1]}|{board[3]}")
   print("-+-+-")
   print(f"{board[3]}|{board[4]}|{board[5]}")
   print("-+-+-")
   print(f"{board[6]}|{board[7]}|{board[8]}")
   print()

def its_a_tie(board):
   for square in range(9):
      if board[square] != "x" and board[square] != "o":
         return False
   return True

def we_have_a_winner(board):
   return (board[0] == board[1] == board[2] or
           board[3] == board[4] == board[5] or
           board[6] == board[7] == board[8] or
           board[0] == board[3] == board[6] or
           board[1] == board[4] == board[7] or
           board[2] == board[5] == board[8] or
           board[0] == board[4] == board[8] or
           board[2] == board[4] == board[6]) 

def your_move(player, board):
   square = int(input(f"{player}'s turn to choose a square (1-9): "))
   board[square - 1] == player

if __name__ == "__main__":
    main()