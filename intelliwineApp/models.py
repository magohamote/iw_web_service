from django.db import models


WINE_COLOR = (
    ('0', 'red'),
    ('1', 'white'),
    ('2', 'pink'),
    ('3', 'gold'),
)


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Bottle(models.Model):
    name = models.CharField()
    color = models.CharField(choices=WINE_COLOR)
    year = models.IntegerField()

