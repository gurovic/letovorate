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

class Task(models.Model):
    title = models.CharField(max_length=20, verbose_name="Задача")
    order = models.IntegerField(verbose_name="Порядок")
    subject = models.ForeignKey(Subject, verbose_name="Предмет")
    round = models.ForeignKey(Round, verbose_name="Раунд")
    grade = models.IntegerField(verbose_name="Класс")

    def __str__(self):
        return "{} класс, {}, {}, задача {}".format(self.grade, self.subject,
                    self.round, self.title)


class Mark(models.Model):
    task = models.ForeignKey(Task, verbose_name="Задача")
    student_id = models.IntegerField(verbose_name="ID участника")
    value = models.IntegerField(verbose_name="Оценка")
    time = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время проверки")
    examiner = models.ForeignKey(Examiner, verbose_name="Экзаменатор") 

    def __str__(self):
        return "{} for {} to student #{}".format(self.value, self.task, self.student_id)
