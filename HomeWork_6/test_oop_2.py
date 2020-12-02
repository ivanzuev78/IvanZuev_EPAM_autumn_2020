from copy import copy

import pytest
from mock import patch, Mock
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
    homework_result = student.do_homework(homework, "BAD!")
    assert Teacher.check_homework(homework_result) is False


@pytest.fixture
def outdated_homework():
    return Teacher.create_homework("Learn functions", 1)


@patch("HomeWork_6.oop_2.datetime")
def test_student_do_homework_not_in_time(datetime_mock, student, outdated_homework):
    datetime_mock.datetime.now = Mock(
        return_value=datetime.datetime.now() + datetime.timedelta(3)
    )
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(outdated_homework, "I must hurry up!")


def test_check_homework_doesnt_stack_same_hw():
    hw_result = Student("Ivan", "Zuev").do_homework(
        Teacher.create_homework("Task of HW", 1), "I have done this hw"
    )

    Teacher.check_homework(hw_result)
    dict_of_homeworks_after_1_accepted_work = copy(Teacher.homework_done)
    Teacher.check_homework(hw_result)
    dict_of_homeworks_after_2_accepted_same_works = copy(Teacher.homework_done)

    assert (
        dict_of_homeworks_after_1_accepted_work
        == dict_of_homeworks_after_2_accepted_same_works
    )


def test_reset_results_of_homeworks():
    homework_1 = Teacher.create_homework("Task of HW", 1)
    good_student = Student("Ivan", "Zuev")
    hw_result_1 = good_student.do_homework(homework_1, "Some answer")
    Teacher.check_homework(hw_result_1)
    assert Teacher.homework_done
    Teacher.reset_results()
    assert Teacher.homework_done == defaultdict(list)
