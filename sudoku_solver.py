board = [
  [0,0,0, 0,0,0, 0,0,0],
  [0,0,0, 0,0,0, 0,0,0],
  [0,0,0, 0,0,0, 0,0,0],
  
  [0,0,0, 0,0,0, 0,0,0],
  [0,0,0, 0,0,0, 0,0,0],
  [0,0,0, 0,0,0, 0,0,0],
  
  [0,0,0, 0,0,0, 0,0,0],
  [0,0,0, 0,0,0, 0,0,0],
  [0,0,0, 0,0,0, 0,0,0]


]
  
def p_board(bo):
  for i in range(len(bo)):
    if i % 3 == 0 and i != 0:
      print("———+———+———")
    for j in range(len(bo[0])):
      if j % 3 == 0 and j != 0:
        print("|",end=" ")
      print(board[i][j],end=" ")
    print()
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
p_board(board)
        
