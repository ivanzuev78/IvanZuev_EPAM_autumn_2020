import pytest

from HomeWork_6.oop_2 import *


@pytest.fixture
def teacher():
    yield Teacher("Daniil", "Shadrin")


@pytest.fixture
def student():
    yield Student("Roman", "Petrov")


def test_create_teacher(teacher):
    assert teacher.first_name == "Daniil"
    assert teacher.last_name == "Shadrin"


def test_create_student(student):
    assert student.first_name == "Roman"
    assert student.last_name == "Petrov"


def test_homework_is_created(teacher):
    homework = teacher.create_homework("Learn functions", 1)
    assert homework.text == "Learn functions"
    assert homework.is_active() is True


def test_homework_deadline():
    homework = Teacher.create_homework("task", 5)
    assert homework.deadline == datetime.timedelta(5)


def test_student_do_homework_in_time_good_hw(student):
    homework = Teacher.create_homework("Learn functions", 1)
    homework_result = student.do_homework(homework, "Homework is done")
    assert Teacher.check_homework(homework_result) is True


def test_student_do_homework_in_time_bad_hw(student):
    homework = Teacher.create_homework("Learn functions", 1)
    homework_result = student.do_homework(homework, "done")
    assert Teacher.check_homework(homework_result) is False


@pytest.fixture
def outdated_homework(monkeypatch):
    homework = Teacher.create_homework("Learn functions", 1)
    new_time = datetime.datetime.now() + datetime.timedelta(2)

    class new_datetime:
        @classmethod
        def now(cls):
            return new_time

    monkeypatch.setattr(datetime, "datetime", new_datetime)
    return homework


def test_student_do_homework_not_in_time(student, outdated_homework, capsys):
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(outdated_homework, "I must hurry up!")
