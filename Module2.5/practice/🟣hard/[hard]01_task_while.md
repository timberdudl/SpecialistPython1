## "Число Фибоначчи"

### Задание

По данному числу n определите n-е [число Фибоначчи](https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8).

### Формат входных данных

Дано целое положительное число n, номер числа Фибоначчи в последовательности.

### Формат выходных данных

Вывести число Фибоначчи с номером n.


### Решение задачи

```python
serial_number = int(input('введите номер:'))
count = 0
feb_desired = 0
feb_previous = 1
feb_pre_previous = 0
if serial_number == 2:
    print(1)
else:
    while count < serial_number - 2:
        feb_desired = feb_previous + feb_pre_previous
        feb_pre_previous = feb_previous
        feb_previous = feb_desired
        count += 1
    print(feb_desired)
```

### Данные для самопроверки

| Дано | Результат |
| :---: | --- |
|    1    | 0 |
|    4    | 2 |
|    7    | 8  |
|    11    | 55 |
