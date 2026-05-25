board = [
  ['•','•','•'],
  ['•','•','•'],
  ['•','•','•'],
  ]
def show_board():
  for row in board:
    print(*row)
def isWin(player):
  for row in board:
    if row[0] == row[1] == row[2] == player:
      return True
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] == player:
      return True
  if board[0][0] == board[1][1] == board[2][2] == player:
     return True
  if board[0][2] == board[1][1] == board[2][0] == player:
    return True
  return False
def isDraw():
  for row in board:
    if '•' in row:
      return False
  return True
def input_player():
  row=int(input(f'Masukkan Baris : ' ))
  col=int(input(f'Masukkan Kolom : ' ))
  return row-1,col-1
def minimax(isMaximizing):
  if isWin(AI):
    return 1
  if isWin(Human):
    return -1
  if isDraw():
    return 0
  if isMaximizing:
    bestscore=-5
    for row in range(3):
      for col in range(3):
        if board[row][col] == '•':
           board[row][col] = AI
           score=minimax(False)
           board[row][col] = '•'
           if score>bestscore:
             bestscore=score
    return bestscore
  else:
    bestscore=5
    for row in range(3):
      for col in range(3):
        if board[row][col] == '•':
          board[row][col] = Human
          score=minimax(True)
          board[row][col] = '•'
          if score<bestscore:
            bestscore=score
    return bestscore
          
def ai_move():
  bestscore=-5
  move=None
  for row in range(3):
    for col in range(3):
        if board[row][col] == '•':
           board[row][col] = AI
           score=minimax(False)
           board[row][col] = '•'
           if score>bestscore:
             bestscore=score
             move=(row,col)
  return move
  
Human='X'
AI='O'
player1='X'
player2='0'
player=Human
while True:
  play=int(input('1.Bermain Dengan AI \n2.Bermain Dengan Player \n'))
  if play == 2:
    while True:
      print(f'Pemain "{player}" Bermain!')
      show_board()
      r,c=input_player()
      if board[r][c] != '•':
        print('TEMPAT SUDAN DI ISI!')
        continue
      board[r][c]=player
      if isWin(player):
        show_board()
        print(f'PEMAIN "{player}" MENANG')
        break
      if isDraw():
        show_board()
        print(f'PERMAINAN SERI!')
        break
      if player == Human:
        player=AI
      else:
        player=Human
  elif play == 1:
    while True:
      print(f'Pemain "{player}" Bermain!')
      show_board()
      if player == Human:
        r,c=input_player()
        if board[r][c] != '•':
          print('Tempat sudah di isi!')
          continue
      if player == AI:
        r,c=ai_move()
      board[r][c]=player
      if isWin(player):
        show_board()
        print(f'PEMAIN "{player}" MENANG')
        break
      if isDraw():
        show_board()
        print(f'PERMAINAN SERI!')
        break
      if player == Human:
        player=AI
      else:
        player=Human
  while True:
    val=input('Apakah ingin bermain lagi(y/n)')
    if val == 'n':
      break
    elif val == 'y':
      board = [
  ['•','•','•'],
  ['•','•','•'],
  ['•','•','•'],
  ]
      break
    else:
      print('Input tidak sesuai')
  if val == 'n':
    break