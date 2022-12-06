class Cell:

    def __init__(self, number_cell):
        self.number_cell = number_cell
        self.sim = str(number_cell)

    def free_busy(self, sim):
        self.sim = sim


class Board:
    win_sim = None
    board = {}
    for i_num in range(1, 10):
        board[i_num] = Cell(i_num)

    def __repr__(self):
        return f'| {board.board[1].sim} | {board.board[2].sim} | {board.board[3].sim} |\n'\
               f'| {board.board[4].sim} | {board.board[5].sim} | {board.board[6].sim} |\n'\
               f'| {board.board[7].sim} | {board.board[8].sim} | {board.board[9].sim} |'


class Player:
    cell_occupation = []

    def __init__(self, name, board_pl, sim):
        self.name = name
        self.board = board_pl
        self.sim = sim

    def goes(self, num_cell):
        if self.board.board[num_cell] not in self.cell_occupation:
            self.board.board[num_cell].free_busy(sim=self.sim)
            self.cell_occupation.append(self.board.board[num_cell])
        else:
            print('Клетка уже занята')
            self.goes(num_cell=int(input('выберите клетку (1-9)\n')))

    def win(self):
        win_1 = ([self.board.board[1].sim, self.board.board[2].sim, self.board.board[3].sim])
        win_2 = ([self.board.board[4].sim, self.board.board[5].sim, self.board.board[6].sim])
        win_3 = ([self.board.board[7].sim, self.board.board[8].sim, self.board.board[9].sim])
        win_4 = ([self.board.board[1].sim, self.board.board[5].sim, self.board.board[9].sim])
        win_5 = ([self.board.board[2].sim, self.board.board[5].sim, self.board.board[8].sim])
        win_6 = ([self.board.board[3].sim, self.board.board[5].sim, self.board.board[7].sim])
        win_list = [win_6, win_5, win_4, win_3, win_2, win_1]
        for i_win in win_list:
            sim = ''
            for j_win in i_win:
                sim += j_win
            if sim == self.sim * 3:
                self.board.win_sim = self.sim
                return True


board = Board()
player_1 = Player(input('Имя первого игрока: '), board, input('\nВведет знак'))
player_2 = Player(input('Имя второго игрока: '), board, input('\nВведет знак'))
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
