
from django.db import models
import datetime


class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE,)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return str(self.date)


"""
class Kurs(models.Model):
    kurs_name = models.CharField(max_length=264,unique=True)
    kurs_url = models.URLField(unique=True)
    kurs_date = models.DateField()

    def __init__(self):
        self.kurs_id = functions.give_id(1)

    def __str__(self):
        return self.kurs_name

class Frage(models.Model):
    kurs_id = models.ForeignKey(Kurs,on_delete=models.CASCADE,)
    frage_name = models.CharField(max_length=264,unique=True)
    frage_date = models.DateField()

    def __init__(self):
        self.frage_id = functions.give_id(2)


    def __str__(self):
        return self.kurs_id

class Choises(models.Model):
    frage_id = models.ForeignKey(Frage,on_delete=models.CASCADE,)
    choises_list = []
    right = []

    def __str__(self):
        return self.right
"""
