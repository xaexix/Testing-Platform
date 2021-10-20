from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    TEACHER = 1
    STUDENT = 0
    ROLES_CHOICES = (
        (TEACHER, 'Учитель'),
        (STUDENT, 'Ученик'),
    )
    role = models.CharField(
        max_length=30,
        verbose_name='Роль',
        choices=ROLES_CHOICES,
        default=STUDENT
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Topic(models.Model):
    subject = models.ForeignKey(
        'Subject',
        verbose_name='Предмет',
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=150,
        verbose_name='Название темы',
    )
    question = models.ForeignKey(
        'Question',
        verbose_name='Вопрос',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    owner = models.ForeignKey(
        'User',
        verbose_name='Создатель',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема тестов'
        verbose_name_plural = 'Темы тестов'


class Subject(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Название',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Question(models.Model):
    problem = models.TextField(verbose_name='Задача')
    answer = models.ForeignKey(
        'Answer',
        verbose_name='Ответ',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.problem

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Answer(models.Model):
    text = models.TextField(verbose_name='Ответ')
    is_correct = models.BooleanField(
        verbose_name='Правильный ответ',
        default=False,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
