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
    return Teacher.create_homework("Learn functions", 0)


def test_student_do_homework_not_in_time(student, outdated_homework):
    with pytest.raises(DeadlineError, match="You are late"):
        student.do_homework(outdated_homework, "I must hurry up!")


def test_check_homework_doesnt_stack_same_hw(student, teacher):
    hw_result = student.do_homework(
        teacher.create_homework("Task of HW", 1), "I have done this hw"
    )
    hw_result_2 = student.do_homework(
        teacher.create_homework("Task of HW_2", 1), "I have done this hw too"
    )
    teacher.check_homework(hw_result)
    dict_of_homeworks_after_1_accepted_work = copy(teacher.homework_done)
    teacher.check_homework(hw_result)

    dict_of_homeworks_after_2_accepted_same_works = copy(teacher.homework_done)

    assert (
        dict_of_homeworks_after_1_accepted_work
        == dict_of_homeworks_after_2_accepted_same_works
    )

    teacher.check_homework(hw_result_2)
    dict_of_homeworks_after_2_accepted_same_works_and_1_another_hw = copy(
        teacher.homework_done
    )
    assert (
        dict_of_homeworks_after_2_accepted_same_works
        != dict_of_homeworks_after_2_accepted_same_works_and_1_another_hw
    )


def test_reset_results_of_homeworks(student, teacher):
    homework_1 = teacher.create_homework("Task of HW", 1)
    hw_result_1 = student.do_homework(homework_1, "Some answer")
    teacher.check_homework(hw_result_1)
    assert Teacher.homework_done
    teacher.reset_results()
    assert not Teacher.homework_done
