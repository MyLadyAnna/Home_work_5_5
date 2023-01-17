# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

import random

def player_round(max_num, num, player):                          # фун для игрока
    take_candy = -1
    while 0 > take_candy or take_candy > max_num or take_candy > num:
        take_candy = int(input(f'Сколько конфет из {num} возмет игрок {player}? '))
        if take_candy > max_num:                                    
            print(f'Максимально количество конфет, которые можно взять -  {max_num}!')
        elif take_candy > num:
            print(f'Осталось всего {num} кофет!')
        elif take_candy == 0:
            print(f'Надо взять минимум одну конфету!')
    return take_candy

def bot_round(max_num, num):                                      # фун для бота
    if num <= max_num:                                            # если 28 и меньше
        take_candy = num
    elif num > max_num and num - max_num <= max_num + 1:          # если остается от 57 и ниже. 
        take_candy = num - (max_num + 1)                          # чтобы выиграть боту, надо оставить после себя 29 конфет (т к по условию больше 28 нельзя)
    else: 
        take_candy = random.randint(1,max_num)                    # до 57
    print(f'Бот берет {take_candy} конфет(у).')
    return take_candy  

candy = int(input('Введите количество конфет на столе: '))
max_candy = 28          # max_candy = int(input('Введите максимальное количество конфет, которое можно взять за 1 ход: ')) - если менять в условии число 28
print(f'  Игра с конфетам. На столе лежит {candy} конфет(а). Играют два игрока делая ход друг после друга. \
Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем {max_candy} конфет. \
Все конфеты оппонента достаются сделавшему последний ход. \n Если хотите играть с ботом - введите имя "bot".')
p_name = []
p_name.append(input("Имя первого игрока: "))
p_name.append(input("Имя второго игрока: "))

in_game_player = random.randint(0,1)

print(f'Первым ходит игрок {p_name[in_game_player]}')
   
game_candy = candy

while game_candy > 0:
    if 'bot' not in p_name[in_game_player]:
        game_candy -= player_round(max_candy, game_candy, p_name[in_game_player])
    else:
        game_candy -= bot_round(max_candy, game_candy)
    print(f'Осталось конфет - {game_candy}.')
    in_game_player = int(not bool(in_game_player))
print(f'Победил игрок {p_name[int(not bool(in_game_player))]}!')
