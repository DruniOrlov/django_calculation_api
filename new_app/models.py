from django.db import models


class Calculations(models.Model):
    date = models.DateField()
    liquid = models.FloatField()
    oil = models.FloatField()
    water = models.FloatField()
    wct = models.FloatField()

