# Бегун проводил ежедневные тренировки и записывал расстояния которые пробегал за занятия в метрах:
distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
# Переведите все значения в футы (получить и вывести новый список)

distances = [600, 755, 321.6, 1234, 231, 456.6, 4561, 1200, 456]
distances_in_feet = []
for distance in distances:
    distances_in_feet.append(round(float(distance) * 3.28, 2))
print(distances_in_feet)
