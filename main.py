board = [['_','_','_'],
   ['_','_','_'],
   ['_','_','_']]

symbols = ['X', 'O']
turn = 0

def welcome_screen():
  print('Welcome to')
  print(''' ______    ______      ______ 
(  /o     (  /        (  /    
  /,  _,    /__,  _,    /__ _ 
_/ (_(__  _/(_/(_(__  _/(_)(/_
                              
                              ''')

# Prints the board
def print_board():
  for row in board:
    for col in row:
      print(col, end=' ')
    print()

# Inserts a move at a given row & column
def make_move(row, col, symbol):
  if(board[row][col] != ('_')):
    print("Spot taken. Pick another one.")
    change_turn()

  else:
    board[row][col] = symbol

# Returns true when the game is over 
# Note: Just a stub. Doesn't work yet
def is_game_over():
  is_over = False
  
  for i in board:

    is_over = all(n == "X" for n in i)
    if is_over:
      print_board()
      return True
    is_over = all(n == "O" for n in i)
    if is_over:
      print_board()
      return True

  for i in range(3):
    column = [col[i] for col in board]
    column = set(column)
    column = list(column)

    if len(column) == 1 and column[0] == "X":
      print_board()
      return True
      
    if len(column) == 1 and column[0] == "O":
      print_board()
      return True
    is_over = False

  if board[0][2] == board[1][1] and board[1][1] == board [2][0] and board[0][2] != "_":
    print_board()
    return True
  if board[0][0] == board[1][1] and board[1][1] == board [2][2] and board[0][0] != "_":
    print_board()
    return True
    
  return is_over

# Alternates the turn between 0 and 1
def change_turn():
  global turn
  turn = (turn + 1) % 2

welcome_screen()
while not is_game_over():
  # Print the board and whose turn it is
  print_board()
  print('Player {}'.format(turn+1))
  
  # Get the user input

  v = 0
  while v == 0:
   row_choice = int(input('Which row would you like to choose? '))
   if(row_choice < 0 or row_choice > 2):
     print("Invalid choice try again")
   else:
     v = 1
  v = 0
  while v == 0:
   col_choice = int(input('Which column would you like to choose? '))
   if(col_choice < 0 or col_choice > 2):
     print("Invalid choice try again")
   else:
     v = 1

  # Put their move on the board
  make_move(row_choice, col_choice, symbols[turn])
  
  # Next turn
  change_turn()
