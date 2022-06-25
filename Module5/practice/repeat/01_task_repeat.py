# Напишите функцию, создающую(возвращающую) список заданной длины заполненный
# произвольными целыми числами в заданном диапазоне.
# , где size - размер генерируемого списка c элементами в диапазоне от of до to.

def gen_list(size, up=-10, to=10):
    import random
    my_list = []
    for _ in range(size):
        number = random.randint(up, to)
        my_list.append(number)
    return my_list

