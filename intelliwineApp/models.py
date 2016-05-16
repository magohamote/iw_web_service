from django.db import models


owner = models.ForeignKey('auth.User', related_name='bottles')
highlighted = models.TextField()


class TestClass(models.Model):
    test = models.IntegerField()


class BottleDNA(models.Model):
    clarity = models.CharField(max_length=16)
    colorSimple = models.CharField(max_length=10)
    color = models.CharField(max_length=16)
    observations1 = models.CharField(max_length=256)
    condition = models.CharField(max_length=16)
    intensity = models.CharField(max_length=16)
    aromaCharacteristic = models.CharField(max_length=2048)
    development = models.CharField(max_length=32)
    sweetness = models.CharField(max_length=16)
    acidity = models.CharField(max_length=16)
    tanning = models.CharField(max_length=16)
    alcohol = models.CharField(max_length=16)
    body = models.CharField(max_length=16)
    flavourIntensity = models.CharField(max_length=16)
    flavourCharacteristic = models.CharField(max_length=2048)
    observations2 = models.CharField(max_length=256)
    finish = models.CharField(max_length=16)
    qualityLevel = models.CharField(max_length=16)
    structure = models.CharField(max_length=256)
    balance = models.CharField(max_length=256)
    concentration = models.CharField(max_length=256)
    complexity = models.CharField(max_length=256)
    length = models.CharField(max_length=256)
    typicity = models.CharField(max_length=256)
    levelOfReadiness = models.CharField(max_length=64)
    appellation = models.CharField(max_length=256)
    region = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    variety = models.CharField(max_length=256)
    vintage = models.CharField(max_length=256)
    productionMethod = models.CharField(max_length=256)
    climaticInfluences = models.CharField(max_length=256)
    nameOfTheWine = models.CharField(max_length=256)
    nameOfTheWinery = models.CharField(max_length=256)
    typeOfSweetness = models.CharField(max_length=16)
    typeOfCarbonDioxide = models.CharField(max_length=16)
    typeOfViscosity = models.CharField(max_length=16)
    typeOfAlcohol = models.CharField(max_length=16)
    typeOfAcid = models.CharField(max_length=16)
    typeOfFruit = models.CharField(max_length=16)
    typeOfTannin = models.CharField(max_length=16)
    ripeness = models.CharField(max_length=16)
    freshness = models.CharField(max_length=16)
    harmony = models.CharField(max_length=16)

    class Meta:
        ordering = ('nameOfTheWine',)

