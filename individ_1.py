#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#   Выполнить индивидуальное задание 1 лабораторной работы 12, максимально задействовав
#   имеющиеся в Python средства перегрузки операторов.


class Triangle:

    def __init__(self, first=1, second=1, third=1):
        first = float(first)
        second = float(second)
        third = float(third)

        self.__first = first
        self.__second = second
        self.__third = third

        if first <= 0 or second <= 0 or third <= 0:
            raise ValueError("Ошииибка!!!")

    # Ввод сторон треугольника
    def read(self):
        first = input('Введите первую сторону треугольника: ')
        second = input('Введите вторую сторону треугольника: ')
        third = input('Введите третью сторону треугольника: ')

        self.__first = float(first)
        self.__second = float(second)
        self.__third = float(third)

        self.add()
        self.square()

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        self.__first = float(value)

    @property
    def second(self):
        return self.__second

    @property
    def third(self):
        return self.__third

    # Привести числа к строке.
    def __str__(self):
        return f"{self.__first} + {self.__second} + {self.__third}"

    def __repr__(self):
        return self.__str__()

    # Привести числа к вещественному значению.
    def __float__(self):
        return self.__first + self.__second + self.__third

    # Сложение чисел.
    def __iadd__(self, rhs):  # +=
        if isinstance(rhs, Triangle):
            first = self.first + self.second + self.third
            self.__first, self.__second, self.third = first
            return self
        else:
            raise ValueError("Illegal type of the argument")

    # Вычисление периметра треугольника
    def add(self):
        self.perimeter = self.__first + self.__second + self.__third
        return self.perimeter

    # Вычисление площади треугольника
    def square(self):
        p = self.perimeter / 2
        self.s = math.sqrt(p * (p - self.__first) * (p - self.__second) * (p - self.__third))
        return self.s

    # Сравнение площадей треугольников
    def __lt__(self, other):
        return self.s < other.s

    def __gt__(self, other):
        return self.s > other.s

    def __le__(self, other):
        return self.s <= other.s

    def __ge__(self, other):
        return self.s >= other.s

    def __eq__(self, other):
        return self.s == other.s

    def __add__(self, other):
        return self.s + other.s

    def __sub__(self, other):
        if self.s >= other.s:
            return self.s - other.s
        else:
            return ValueError("Отрицательная площадь! -_-")

    def __mul__(self, other):
        return self.s * other.s

    def __truediv__(self, other):
        return self.s / other.s

    def __ne__(self, other):
        return self.s != other.s


if __name__ == '__main__':
    r1 = Triangle()
    r1.read()
    r2 = Triangle()
    r2.read()
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





