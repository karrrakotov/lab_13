#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Rational:

    def __init__(self, first=0, second=0, third=0):

        self.first = int(first)
        self.second = int(second)
        self.third = int(third)

        self.first = first
        self.second = second
        self.third = third



    # Клонировать дробь.
    def __clone(self):
        return Rational(self.first, self.second, self.third)

    @property
    def first(self):
        return self.first

    @first.setter
    def first(self, value):
        self.__first = int(value)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        value = int(value)
        if value == 0:
            raise ValueError("Illegal value of the denominator")
        self.__second = value

    @property
    def third(self):
        return self.third

    @third.setter
    def third(self, value):
        self.__third = int(value)

    # Привести дробь к строке.
    def __str__(self):
        return f"{self.__first}, {self.__second}, {self.__third}"

    def __repr__(self):
        return self.__str__()

    # Привести дробь к вещественному значению.
    def __float__(self):
        return self.__numerator, self.__denominator, self.__third

    # Сложение обыкновенных дробей.
    def __iadd__(self, rhs):  # +=
        if isinstance(rhs, Rational):
            global perimeter
            perimeter = self.first + self.second + self.third

            return perimeter
        else:
            raise ValueError("Illegal type of the argument")

    def __add__(self, rhs):  # +
        return self.__clone().__iadd__(rhs)



if __name__ == '__main__':
    r1 = Rational(3, 4, 5)
    print(f"r1 = {r1}")
    r2 = Rational(5, 6, 3)
    print(f"r2 = {r2}")
    print(f"r1 + r2 = {r1 + r2}")

