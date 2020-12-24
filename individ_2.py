#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from dataclasses import dataclass, field
from typing import List
import xml.etree.ElementTree as ET


#   Для варианта задания лабораторной работы 8 необходимо дополнительно
#   реализовать сохранение и чтение данных из файла формата JSON. Необходимо проследить за
#   тем, чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
#   работы.


@dataclass(frozen=True)
class Person:
    name: str
    group: str
    marks: list


@dataclass
class Staff:
    students: List[Person] = field(default_factory=lambda: [])

    def add(self, name, group, marks):
        self.students.append(
            Person(
                name=name,
                group=group,
                marks=marks
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
                    person.marks[0],
                    person.marks[1],
                    person.marks[2],
                    person.marks[3],
                    person.marks[4]
                )
            )
        table.append(line)

        return '\n'.join(table)

    @staticmethod
    def select():
        result = []
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

            if 5 > marks[0] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[1] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[2] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[3] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            if 5 > marks[4] < 2:
                print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
                exit(1)

            staff.add(name, group, marks)

        elif command == 'list':
            print(staff)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            selected = staff.select(parts[1])
            count = 0

            if selected:
                for count, person in enumerate(selected, 1):
                    print(
                        '{:>4}: {}'.format(count, person.name)
                    )

        elif command.startswith('load '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Прочитать данные из файла JSON.
            staff.load(parts[1])

        elif command.startswith('save '):
            # Разбить команду на части для выделения имени файла.
            parts = command.split(' ', maxsplit=1)
            # Сохранить данные в файл JSON.
            staff.save(parts[1])

        elif command == 'help':
            # Вывести справку о работе с программой.
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