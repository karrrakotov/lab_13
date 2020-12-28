#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#   Выполнить индивидуальное задание 1 лабораторной работы 12, максимально задействовав
#   имеющиеся в Python средства перегрузки операторов.


class Triangle:

    def __init__(self, first=1, second=1, third=1, square=1):
        self.__first = float(first)
        self.__second = float(second)
        self.__third = float(third)
        self.__square = float(square)

    # Вывод данных на экран
    def __str__(self):
        return f"{self.__first, self.__second, self.__third, self.__square}"

    # Сравнение площадей треугольников
    def __lt__(self, other):
        return self.__square < other.__square

    def __gt__(self, other):
        return self.__square > other.__square

    def __le__(self, other):
        return self.__square <= other.__square

    def __ge__(self, other):
        return self.__square >= other.__square

    def __eq__(self, other):
        return self.__square == other.__square

    def __ne__(self, other):
        return self.__square != other.__square

    # Выполнения арефметических операций над площадями
    def __add__(self, other):
        return self.__square + other.__square

    def __sub__(self, other):
        if self.__square >= other.__square:
            return self.__square - other.__square
        else:
            return ValueError("Отрицательная площадь! -_-")

    def __mul__(self, other):
        return self.__square * other.__square

    def __truediv__(self, other):
        return self.__square / other.__square


if __name__ == '__main__':
    r1 = Triangle(first=5, second=4, third=3, square=6)
    print(f"r1 = {r1}")

    r2 = Triangle(first=5, second=5, third=6, square=12)
    print(f"r2 = {r2}")

    print(f"S1 < S2: {r1 < r2}")
    print(f"S1 > S2: {r1 > r2}")
    print(f"S1 <= S2: {r1 <= r2}")
    print(f"S1 >= S2: {r1 >= r2}")
    print(f"S1 = S2: {r1 == r2}")
    print(f"S1 != S2: {r1 != r2}")

    print(f"S1 + S2: {r1 + r2}")
    print(f"S1 - S2: {r1 - r2}")
    print(f"S1 * S2: {r1 * r2}")
    print(f"S1 / S2: {r1 / r2}")
