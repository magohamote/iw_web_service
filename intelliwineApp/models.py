from django.db import models


class Bottle(models.Model):
    name = models.CharField(max_length=250)
    sweetness = models.IntegerField()
    acidity = models.IntegerField()
    tannin = models.IntegerField()
    alcohol = models.IntegerField()
    body = models.IntegerField()
    flavour_intensity = models.IntegerField()
    # each aroma has a line, and value is 0 or 1
