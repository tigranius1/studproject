from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО студента')
    group = models.CharField(max_length=10, verbose_name='Группа')

    def __str__(self):
        return self.name


class Session(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        verbose_name='Студент'
    )
    math = models.IntegerField(verbose_name='Математика')
    physics = models.IntegerField(verbose_name='Физика')
    programming = models.IntegerField(verbose_name='Программирование')

    def __str__(self):
        return f"Оценки {self.student.name}"