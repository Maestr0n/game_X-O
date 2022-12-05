import back

board = back.Board()
player_1 = back.Player(input('Имя первого игрока: '), board, input('\nВведет знак'))
player_2 = back.Player(input('Имя второго игрока: '), board, input('\nВведет знак'))
print(board)
check = True
for _ in range(4):
    winner = board.win_sim
    player_1.goes(int(input(f'{player_1.name} выберите клетку (1-9)\n')))
    print(board)
    if player_1.win():
        break
    player_2.goes(int(input(f'{player_2.name} выберите клетку (1-9)\n')))
    print(board)
    if player_2.win():
        break
else:
    check = False
    player_1.goes(int(input(f'{player_1.name} выберите клетку (1-9)\n')))
    print(board, '\n\nНичя')
if not check:
    if board.win_sim == player_1.sim:
        winner = player_1.name
    else:
        winner = player_2.name
    print('\nПобедил', str(winner).upper())
