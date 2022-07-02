# Дан список, заполненный произвольными целыми числами.
# Примечание: для генерации списка используйте функцию написанную на одном из прошлых занятий.
# Получите новый список, элементами которого будут:
#   1. неповторяющиеся(уникальные) элементы исходного списка:
#   например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
#   2. элементы исходного списка, которые не имеют повторений(встречаются только один раз):
#   например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

import random

numbers = []
quantity = 10
for _ in range(quantity):
    number = random.randint(-10, 10)
    numbers.append(number)
print(numbers)
unique_numbers = []
for number in numbers:
    if number in unique_numbers:
        continue
    unique_numbers.append(number)
once_count_numbers = []
for number in numbers:
    if numbers.count(number) == 1:
        once_count_numbers.append(number)
print(unique_numbers)
print(once_count_numbers)
