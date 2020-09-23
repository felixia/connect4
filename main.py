def connect4(field):
  for row in range(11):
    if row % 2 == 0:
      practical_row = row // 2
      for column in range(13):
        if column % 2 == 0:
          practical_column = column // 2
          if column != 12:
            print(field[practical_column][practical_row], end="")
          else:
            print(field[practical_column][practical_row])
        else:
          print("|", end="")
    else:
      print("-------------")


player = 1
current_field = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "]
                 ]
connect4(current_field)
while(True):
  print('Players turn: ', player)
  move_row = -1
  move_column = int(input('Please Enter the column:\n'))
  if player == 1:
    if move_column == 0:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'X'
        player = 2
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'X'
        player = 2
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'X'
        player = 2
      else:
        current_field[move_column][0] = 'X'
        player = 2
    elif move_column == 1:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'X'
        player = 2
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'X'
        player = 2
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'X'
        player = 2
      else:
        current_field[move_column][0] = 'X'
        player = 2
    elif move_column == 2:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'X'
        player = 2
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'X'
        player = 2
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'X'
        player = 2
      else:
        current_field[move_column][0] = 'X'
        player = 2
    elif move_column == 3:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'X'
        player = 2
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'X'
        player = 2
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'X'
        player = 2
      else:
        current_field[move_column][0] = 'X'
        player = 2
  else:
    if move_column == 0:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'O'
        player = 1
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'O'
        player = 1
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'O'
        player = 1
      else:
        current_field[move_column][0] = 'O'
        player = 1
    elif move_column == 1:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'O'
        player = 1
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'O'
        player = 1
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'O'
        player = 1
      else:
        current_field[move_column][0] = 'O'
        player = 1
    elif move_column == 2:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'O'
        player = 1
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'O'
        player = 1
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'O'
        player = 1
      else:
        current_field[move_column][0] = 'O'
        player = 1
    elif move_column == 3:
      if current_field[move_column][move_row] == " ":
        current_field[move_column][move_row] = 'O'
        player = 1
      elif current_field[move_column][move_row] != " ":
        current_field[move_column][move_row - 1] = 'O'
        player = 1
      elif current_field[move_column][move_row - 1] != " ":
        current_field[move_column][move_row - 2] = 'O'
        player = 1
      else:
        current_field[move_column][0] = 'O'
        player = 1
  connect4(current_field)
