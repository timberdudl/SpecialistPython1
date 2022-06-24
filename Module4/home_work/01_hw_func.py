# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    numbers = []
    numbers += str(ticket_number)
    sum1 = 0
    for number in numbers[:3]:
        sum1 += int(number)
    sum2 = 0
    for number in numbers[3:6]:
        sum2 += int(number)
    return sum1 == sum2
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
