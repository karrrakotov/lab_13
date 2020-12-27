#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from datetime import date
import sys
from typing import List
import xml.etree.ElementTree as ET


@dataclass(frozen=True)
class Person:
    name: str
    group: str
    mark_one: int
    mark_two: int
    mark_three: int
    mark_four: int
    mark_five: int



@dataclass
class Staff:
    students: List[Person] = field(default_factory=lambda: [])

    def add(self, name, group, mark_one, mark_two, mark_three, mark_four, mark_five):
        self.students.append(
            Person(
                name=name,
                group=group,
                mark_one=mark_one,
                mark_two=mark_two,
                mark_three=mark_three,
                mark_four=mark_four,
                mark_five=mark_five
            )
        )
        self.students.sort(key=lambda person: person.name)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 11
        )
        table.append(line)
        table.append(
            '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "1-ая оценка",
                "2-ая оценка",
                "3-ая оценка",
                "4-ая оценка",
                "5-ая оценка"
            )
        )
        table.append(line)

        # Вывести данные о всех сотрудниках.
        for idx, person in enumerate(self.students, 1):
            table.append(
                '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                    idx,
                    person.name,
                    person.group,
                    person.mark_one,
                    person.mark_two,
                    person.mark_three,
                    person.mark_four,
                    person.mark_five
                )
            )
        table.append(line)

        return '\n'.join(table)

    def select(self, period):
        # Получить текущую дату.
        parts = command.split(' ', maxsplit=2)
        period = int(parts[1])
        result = []
        count = 0
        for person in self.students:
            if 2 in person.marks:
                count += 1
                result.append(person)
        return result

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)
        self.students = []

        for person_element in tree:
            name, group, marks = None, None, None

            for element in person_element:
                if element.tag == 'name':
                    name = element.text
                elif element.tag == 'group':
                    group = element.text
                elif element.tag == 'marks':
                    marks = element.text

                if name is not None and group is not None \
                        and marks is not None:
                    self.students.append(
                        Person(
                            name=name,
                            group=group,
                            marks=marks
                        )
                    )

    def save(self, filename):
        root = ET.Element('students')
        for person in self.students:
            person_element = ET.Element('person')

            name_element = ET.SubElement(person_element, 'name')
            name_element.text = person.name

            group_element = ET.SubElement(person_element, 'group')
            group_element.text = person.group

            marks_element = ET.SubElement(person_element, 'marks')
            marks_element = ET.SubElement(marks_element, 'marks')
            #for mark in marks:
                #return mark
            marks_element.text = str(person.marks)

            root.append(person_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':
    # Список работников.
    staff = Staff()

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break
        elif command == 'add':
            # Запросить данные о работнике.
            n = 5
            name = input("Введите фамилию и имя: ")
            group = input("Введите группу: ")
            marks = list(map(int, input("Введите пять оценок студента, в формате - x y z: ").split(None, n)[:n]))
            # Добавить работника.
            staff.add(name, group, marks)
        elif command == 'list':
            # Вывести список.
            print(staff)
        elif command.startswith('select '):
            # Разбить команду на части для выделения номера года.
            parts = command.split(maxsplit=1)
            # Запросить работников.
            selected = staff.select(parts[1])
            # Вывести результаты запроса.
            if selected:
                for count, person in enumerate(selected, 1):
                    print(
                        '{:>4}: {}'.format(count, person.name)
                    )
            else:
                print("Нет студентов, которые получили оценку - 2.")
        elif command.startswith('load '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Загрузить данные из файла.
            staff.load(parts[1])
        elif command.startswith('save '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Сохранить данные в файл.
            staff.save(parts[1])
        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("load <имя файла> - загрузить данные из файла;")
            print("save <имя файла> - сохранить данные в файл;")
            print("select <оценка> - найти студентов которые получили такую оценку;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
