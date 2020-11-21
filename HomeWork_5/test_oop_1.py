import pytest

from HomeWork_5.oop_1 import *


@pytest.fixture
def teacher():
    teacher = Teacher("Daniil", "Shadrin")
    yield teacher


@pytest.fixture
def student():
    student = Student("Roman", "Petrov")
    yield student


def test_create_teacher(teacher):
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_create_student(student):
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_homework_is_created(teacher):
    expired_homework = teacher.create_homework("Learn functions", 1)
    assert expired_homework.text == "Learn functions"
    assert expired_homework.is_active() is True


def test_homework_deadline():
    homework = Teacher.create_homework("task", 5)
    assert homework.deadline == datetime.timedelta(5)


def test_student_do_homework_in_time(student):
    expired_homework = Teacher.create_homework("Learn functions", 1)
    assert student.do_homework(expired_homework) is expired_homework


@pytest.fixture
def outdated_homework(monkeypatch):
    outdated_homework = Teacher.create_homework("Learn functions", 1)
    new_time = datetime.datetime.now() + datetime.timedelta(2)

    class new_datetime:
        @classmethod
        def now(cls):
            return new_time

    monkeypatch.setattr(datetime, "datetime", new_datetime)
    yield outdated_homework


def test_student_do_homework_not_in_time(student, outdated_homework, capsys):
    homework = outdated_homework
    assert student.do_homework(homework) is None
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
