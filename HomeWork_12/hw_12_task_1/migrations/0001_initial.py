# Generated by Django 3.1.5 on 2021-01-15 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomeWork",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("text", models.TextField()),
                ("created_date", models.DateField(auto_now_add=True)),
                ("deadline_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name="HomeWorkResult",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("solution_text", models.TextField()),
                ("solution_date", models.DateField()),
                (
                    "homework_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hw_12_task_1.homework",
                    ),
                ),
                (
                    "student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hw_12_task_1.student",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="homework",
            name="teacher_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="hw_12_task_1.teacher",
            ),
        ),
    ]