"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from typing import Optional


class Homework:
    """
         Homework принимает на вход 2 атрибута: текст задания и количество дней
    на это задание
    Атрибуты:
        text - текст задания
        deadline - хранит объект datetime.timedelta с количеством
        дней на выполнение
        created - c точной датой и временем создания
    Методы:
        is_active - проверяет не истекло ли время на выполнение задания,
        возвращает boolean
    """

    def __init__(self, text: str, deadline: int):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        return self.created + self.deadline > datetime.datetime.now()


class Student:
    """
        2. Student
    Атрибуты:
        last_name
        first_name
    Методы:
        do_homework - принимает объект Homework и возвращает его же,
        если задание уже просрочено, то печатет 'You are late' и возвращает None
    """

    def __init__(self, first_name: str, last_name: str):
        self.last_name = last_name
        self.first_name = first_name

    @staticmethod
    def do_homework(homework: Homework) -> Optional[Homework]:
        if homework.is_active():
            return homework
        print("You are late")
        return None


class Teacher:
    """
        3. Teacher
    Атрибуты:
        last_name
        first_name
    Методы:
        create_homework - текст задания и количество дней на это задание,
        возвращает экземпляр Homework
        Обратите внимание, что для работы этого метода не требуется сам объект.
    """

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def create_homework(text: str, deadline: int) -> Homework:
        return Homework(text, deadline)
