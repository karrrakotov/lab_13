#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#   Выполнить индивидуальное задание 1 лабораторной работы 12, максимально задействовав
#   имеющиеся в Python средства перегрузки операторов.


class Triangle:

    def __init__(self, first=1, second=1, third=1, s=1):
        self.__first = float(first)
        self.__second = float(second)
        self.__third = float(third)
        self.__s = float(s)

    # Сравнение площадей треугольников
    def __lt__(self, other):
        return self.__s < other.__s

    def __gt__(self, other):
        return self.__s > other.__s

    def __le__(self, other):
        return self.__s <= other.__s

    def __ge__(self, other):
        return self.__s >= other.__s

    def __eq__(self, other):
        return self.__s == other.__s

    def __add__(self, other):
        return self.__s + other.__s

    def __sub__(self, other):
        if self.__s >= other.__s:
            return self.__s - other.__s
        else:
            return ValueError("Отрицательная площадь! -_-")

    def __mul__(self, other):
        return self.__s * other.__s

    def __truediv__(self, other):
        return self.__s / other.__s

    def __ne__(self, other):
        return self.__s != other.__s


if __name__ == '__main__':
    r1 = Triangle(5, 4, 3, 6)
    r2 = Triangle(5, 5, 6, 12)

    print(f"Периметр первого треугольника равен: {r1}")
    print(f"Периметр второго треугольника равен: {r2}")
    print(f"S1 < S2: {r1 < r2}")
    print(f"S1 > S2: {r1 > r2}")
    print(f"S1 <= S2: {r1 <= r2}")
    print(f"S1 >= S2: {r1 >= r2}")
    print(f"S1 = S2: {r1 == r2}")
    print(f"S1 + S2: {r1 + r2}")
    print(f"S1 - S2: {r1 - r2}")
    print(f"S1 * S2: {r1 * r2}")
    print(f"S1 / S2: {r1 / r2}")
    print(f"S1 != S2: {r1 != r2}")





