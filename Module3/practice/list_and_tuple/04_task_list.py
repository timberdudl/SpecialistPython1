# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

import random
numbers = []
quantity = 6
for _ in range(quantity):
    number = random.randint(-10, 10)
    numbers.append(number)
print(numbers)
summa = 0
for number in numbers:
    if number % 2 == 0 and number > 0:
        summa += number
print(summa)
