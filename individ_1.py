#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


#   Создать класс Triangle для представления треугольника. Поля данных должны включать
#   углы и стороны. Требуется реализовать операции: получения полей данных,
#   вычисления площади, вычисления периметра, вычисления высот, а также определения
#   вида треугольника (равносторонний, равнобедренный или прямоугольный).

class Triangle:

    def __init__(self, first=0, second=0, third=0):
        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

        self.add()

    # Ввод сторон треугольника
    def read(self):
        first = input('Введите первую сторону треугольника: ')
        second = input('Введите вторую сторону треугольника: ')
        third = input('Введите третью сторону треугольника: ')

        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

        self.add()
        self.square()
        self.height_one()
        self.height_two()
        self.height_three()
        self.corner_one()

    # Вычисление периметра треугольника
    def add(self):
        global perimeter
        perimeter = self.first + self.second + self.third

    # Вычисление площади треугольника
    def square(self):
        p = perimeter / 2
        self.s = math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third))

    # Вычисление высоты проведенной к стороне A
    def height_one(self):
        p = perimeter / 2
        self.h1 = 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.first

    # Вычисление высоты проведенной к стороне B
    def height_two(self):
        p = perimeter / 2
        self.h2 = 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.second

    # Вычисление высоты проведенной к стороне C
    def height_three(self):
        p = perimeter / 2
        self.h3 = 2 * math.sqrt(p * (p - self.first) * (p - self.second) * (p - self.third)) / self.third

    # Вычисление градусов углов по формуле Герона
    def corner_one(self):
        first_corner = math.acos(
            ((self.second ** 2) + (self.third ** 2) - (self.first ** 2)) / (2 * self.third * self.second))
        self.first_degrees = math.degrees(first_corner)

        second_corner = math.acos(
            ((self.first ** 2) + (self.second ** 2) - (self.third ** 2)) / (2 * self.first * self.second))
        self.second_degrees = math.degrees(second_corner)

        third_corner = math.acos(
            ((self.first ** 2) + (self.third ** 2) - (self.second ** 2)) / (2 * self.first * self.third))
        self.third_degrees = math.degrees(third_corner)

        if self.first_degrees == 90 or self.second_degrees == 90 or self.third_degrees == 90:
            print("Треугольник прямоугольный")
        elif self.first_degrees == self.second_degrees or self.first_degrees == self.third_degrees or self.second_degrees == self.third_degrees:
            print("Треугольник равнобедренный")
        elif self.first_degrees == self.second_degrees == self.third_degrees:
            print("Треугольник равносторонний")
        else:
            print("Обычный треугольник")

    def __round__(self):
        self.third_degrees

        # Вывести значения на экран
    def display(self):
        print(f"Периметр треугольника равен: {perimeter}")
        print(f"Площадь треугольника равна: {self.s}")
        print(f"Высота  проведенная к стороне A равна: {self.h1}")
        print(f"Высота  проведенная к стороне B равна: {self.h2}")
        print(f"Высота  проведенная к стороне C равна: {self.h3}")
        print(f"Первый угол в треугольнике равен: {self.first_degrees}")
        print(f"Второй угол в треугольнике равен: {self.second_degrees}")
        print(f"Третий угол в треугольнике равен: {self.third_degrees}")

    # Сравнение площадей треугольников
    def __lt__(self, other):
        return self.s < other.s

    def __gt__(self, other):
        return self.s > other.s

    def __le__(self, other):
        return self.s <= other.s

    def __ge__(self, other):
        return self.s >= other.s


if __name__ == '__main__':
    r1 = Triangle()
    r1.read()
    r1.display()

    r2 = Triangle()
    r2.read()
    r2.display()

    print(f"r1 < r2: {r1 < r2}")
    print(f"r1 > r2: {r1 > r2}")
    print(f"r1 >= r2: {r1 <= r2}")
    print(f"r1 <= r2: {r1 >= r2}")



