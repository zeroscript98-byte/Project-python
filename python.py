board = [
  [0,8,0,3,0,0,0,2,0],
  [0,9,6,0,7,0,0,4,0],
  [0,0,3,0,5,0,0,9,1],
  
  [6,0,0,0,0,0,0,0,3],
  [0,3,0,0,1,5,6,0,0],
  [0,0,0,0,0,0,2,5,4],
  
  [0,0,0,0,0,2,4,0,0],
  [3,7,0,0,0,0,0,0,0],
  [1,0,9,7,0,0,5,0,0]
]
  
def p_board():
  for row in board:
    print(row)
def find_zero():
  for one_row in range(9):
    for one_col in range(9):
      if board[one_row][one_col]==0:
        return one_row,one_col
  return False
def validation(number,row,col):
    for one_col in range(9):
      if board[row][one_col] == number:
        return False
    for one_row in range(9):
      if board[one_row][col] == number:
        return False
    col_box=col // 3
    row_box=row // 3
    for i in range(row_box *3,row_box *3+3):
      for j in range(col_box *3,col_box *3+3):
        if board[i][j] == number:
          return False
    return True
def solving():
  zero=find_zero()
  if zero == False:
    return True
  row,col=zero
  for number in range(1,10):
    if validation(number,row,col):
      board[row][col]=number
      if solving():
        return True
      board[row][col]=0
  return False

solving()
p_board()
    
