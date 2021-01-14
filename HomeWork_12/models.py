from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)


class HomeWork(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    deadline_date = models.DateField()
    teacher_id = models.ForeignKey(Teacher, models.SET_NULL)


class HomeWorkResult(models.Model):
    homework_id = models.ForeignKey(HomeWork, models.CASCADE)
    student_id = models.ForeignKey(Student, models.CASCADE)
    solution_text = models.TextField()
    solution_date = models.DateField()
