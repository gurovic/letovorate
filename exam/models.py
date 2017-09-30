from django.db import models

class Examiner(models.Model):
    fio = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
