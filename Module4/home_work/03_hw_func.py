# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1 = int(input('x1= '))
y1 = int(input('y1= '))
x2 = int(input('x2= '))
y2 = int(input('y2= '))
r1 = int(input('r1= '))
r2 = int(input('r2= '))
print(distance(x1, y1, x2, y2) + r2 <= r1 or distance(x1, y1, x2, y2) + r1 <= r2)
