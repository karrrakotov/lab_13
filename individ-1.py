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

        self.add()

        if first == 0 or second == 0 or third == 0:
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
        self.height_one()
        self.height_two()
        self.height_three()
        self.corner_one()

    # Клонировать числа
    def __clone(self):
        return Triangle(self.__first, self.__second, self.__third)

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
            first = self.first + self.second
            second = rhs.first + rhs.second
            self.__first, self.__second = first, second
            return self
        else:
            raise ValueError("Illegal type of the argument")

    def __add__(self, rhs):  # +
        return self.__clone().__iadd__(rhs)

    # Вычисление периметра треугольника
    def add(self):
        self.perimeter = self.__first + self.__second + self.__third

    # Вычисление площади треугольника
    def square(self):
        p = self.perimeter / 2
        self.s = math.sqrt(p * (p - self.__first) * (p - self.__second) * (p - self.__third))

    # Вычисление высоты проведенной к стороне A
    def height_one(self):
        p = self.perimeter / 2
        self.h1 = 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.first

    # Вычисление высоты проведенной к стороне B
    def height_two(self):
        p = self.perimeter / 2
        self.h2 = 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.second

    # Вычисление высоты проведенной к стороне C
    def height_three(self):
        p = self.perimeter / 2
        self.h3 = 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.third

    # Вычисление градусов углов по формуле Герона
    def corner_one(self):
        a = self.first
        b = self.second
        c = self.third
        first_corner = math.acos(((b ** 2) + (c ** 2) - (a ** 2)) / (2 * c * b))
        self.f_d = math.degrees(first_corner)

        second_corner = math.acos(((a ** 2) + (b ** 2) - (c ** 2)) / (2 * a * b))
        self.s_d = math.degrees(second_corner)

        third_corner = math.acos(((a ** 2) + (c ** 2) - (b ** 2)) / (2 * a * c))
        self.th_d = math.degrees(third_corner)

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

    def __sub__(self, other):
        if self.s >= other.s:
            return self.s - other.s
        else:
            return other.s - self.s


if __name__ == '__main__':
    r1 = Triangle()
    r1.read()
    r2 = Triangle()
    r2.read()

    print(f"Периметр первого треугольника равен: {r1}")
    print(f"Периметр второго треугольника равен: {r2}")
    print(f"S1 - S2 = {r1 - r2}")
    print(f"S1 < S2: {r1 < r2}")
    print(f"S1 > S2: {r1 > r2}")
    print(f"S1 <= S2: {r1 <= r2}")
    print(f"S1 >= S2: {r1 >= r2}")
    print(f"S1 = S2: {r1 == r2}")



