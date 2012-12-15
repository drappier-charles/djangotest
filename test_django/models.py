#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Sondage(models.Model):
    question = models.CharField(max_length=200)
    date_publication = models.DateTimeField()

class Reponse(models.Model):
    sondage = models.ForeignKey(Sondage)
    choix = models.CharField(max_length=200)
    nb_votes = models.IntegerField()