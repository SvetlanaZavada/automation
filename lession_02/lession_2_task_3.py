import math


def area_square(side):
    return math.ceil(side*side)


side = float(input("Введите число"))
print(f"Площадь квадрата: {area_square(side)}")
