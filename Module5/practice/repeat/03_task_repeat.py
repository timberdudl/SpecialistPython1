# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def palindrome_quantity(up=0, to=1000):
    counter = 0
    for number in range(up, to):
        number = str(number)
        if number == number[::-1]:
            counter += 1
    return counter


print(palindrome_quantity(10, 1000))
