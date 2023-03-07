from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя студента')
    age = models.IntegerField(verbose_name='Возраст студента')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Название группы')

    objects = models.Manager

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студента'


class Discipline(models.Model):
    discipline = models.CharField(max_length=50, verbose_name='Название дисциплины')

    objects = models.Manager

    def __str__(self):
        return self.discipline

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class Group(models.Model):
    group = models.CharField(max_length=50, verbose_name='Название группы')

    objects = models.Manager

    def __str__(self):
        return self.group

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Mark(models.Model):
    markch = (('н', 'н'), ('2', 2), ('3', '3'), ('4', '4'), ('5', '5'))
    student = models.ForeignKey('Student', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Имя студента')
    mark = models.CharField(max_length=1, choices=markch, verbose_name='Оценка')
    lesson = models.ForeignKey('Lesson', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Имя урока')

    objects = models.Manager

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'


class Lesson(models.Model):
    discipline = models.ForeignKey('Discipline', on_delete=models.PROTECT, null=True, blank=True,
                                   verbose_name='Название Дисциплины')
    date = models.DateField(verbose_name='Дата получения оценки')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True,
                              verbose_name='Название Группы')

    objects = models.Manager

    def __str__(self):
        return f'{self.date} {self.discipline}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
