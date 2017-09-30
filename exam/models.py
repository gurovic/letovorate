from django.db import models

class Subject(models.Model):
    title = models.CharField(max_length=200,verbose_name="Название")

    def __str__(self):
        return self.title

class Round(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return self.title

class Examiner(models.Model):
    fio = models.CharField(max_length=200, verbose_name="Фамилия, имя, отчество")
    email = models.CharField(max_length=200, verbose_name="E-mail")
    subject = models.ForeignKey(Subject, verbose_name="Предмет")
    round = models.ForeignKey(Round, verbose_name="Раунд")
    grade = models.IntegerField(verbose_name="Класс")
    code = models.CharField(max_length=6, verbose_name="Код доступа")
    grade = models.IntegerField(verbose_name="Класс")

    def __str__(self):
        return self.fio
