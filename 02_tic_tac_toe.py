# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

print('Играем в крестики-нолики!')

board = list(range(1,10))

def draw_a_board(board):
    print('-'*13)
    for i in range(3):
        print(f'| {board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]} |')
        print('-'*13)

def choice(tic_tac):
    flag = False
    while not flag:
        player_index = input(f'Выберите цифру клетки {tic_tac} --> ')
        try:
            player_index = int(player_index)
        except:
            print('Необходимо ввести цифру')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'XO'):
                board[player_index-1] = tic_tac
                flag = True
            else:
                print('Здесь уже что-то стоит')
        else:
            print('Введите цифру, сответствующую значению в какой-либо в клетке')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def game(board):
    counter = 0
    vic = False
    while not vic:
        draw_a_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter += 1
        if counter > 4:
            win = victory_check(board)
            if win:
                print(f'{win} победил')
                vic = True
                break
            if counter == 9:
                print('Ничья!)')
                break
        #draw_a_board(board)

game(board)