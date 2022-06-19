# Вывод символов по диагоналям
# Даны сторона квадрата. Вывести его диагонали символами #.
# Формат входных данных: На вход программе одно целое число a (2<a≤30) - сторона квадрата.
# Формат выходных данных: Требуется вывести диагонали символами # (см. примеры)
# Примеры:
# a = 6
#    #
 #  #
  ##
  ##
 #  #
#    #

# a = 3
# #
 #
# #


square_size = int(input('введите длину стороны квадрата: '))
num_pre_spaces = -1
num_betw_spaces = square_size
if square_size % 2 == 0:
    while num_betw_spaces > 0:
        num_betw_spaces -= 2
        num_pre_spaces += 1
        print(' ' * num_pre_spaces, '#', ' ' * num_betw_spaces, '#', sep = '')
    while num_betw_spaces <= square_size - 2:
        print(' ' * num_pre_spaces, '#', ' ' * num_betw_spaces, '#', sep = '')
        num_pre_spaces -= 1
        num_betw_spaces += 2
if square_size % 2 == 1:
    while num_betw_spaces > 1:
        num_betw_spaces -= 2
        num_pre_spaces += 1
        print(' ' * num_pre_spaces, '#', ' ' * num_betw_spaces, '#', sep = '')
    print(' ' * (square_size // 2), '#', sep = '')
    while num_betw_spaces <= square_size - 2:
        print(' ' * num_pre_spaces, '#', ' ' * num_betw_spaces, '#', sep = '')
        num_pre_spaces -= 1
        num_betw_spaces += 2
