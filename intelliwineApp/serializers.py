# ModelSerializer classes don't do anything particularly magical,
# they are simply a shortcut for creating serializer classes:
#   - An automatically determined set of fields.
#   - Simple default implementations for the create() and update() methods.
from math import sqrt

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import BottleDNA, TestClass, BottleVector


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BottleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BottleDNA
        fields = ('clarity', 'colorSimple', 'color', 'observations1', 'condition', 'intensity', 'aromaCharacteristic',
                  'development', 'sweetness', 'acidity', 'tanning', 'alcohol', 'body', 'flavourIntensity',
                  'flavourCharacteristic', 'observations2', 'finish', 'qualityLevel', 'structure', 'balance',
                  'concentration', 'complexity', 'length', 'typicity', 'levelOfReadiness', 'appellation', 'region',
                  'country', 'variety', 'vintage', 'productionMethod', 'climaticInfluences', 'nameOfTheWine',
                  'nameOfTheWinery', 'typeOfSweetness', 'typeOfCarbonDioxide', 'typeOfViscosity', 'typeOfAlcohol',
                  'typeOfAcid', 'typeOfFruit', 'typeOfTannin', 'ripeness', 'freshness', 'harmony')

    @staticmethod
    def cosine_similarity(x, y):
        numerator = sum(a * b for a, b in zip(x, y))
        denominator = sqrt(sum([a * a for a in x])) * sqrt(sum([a * a for a in y]))
        return numerator / float(denominator)


class TestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TestClass
        fields = ('test',)


class BottleVectorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = BottleVector
        fields = ('intensity', 'aromaCharacteristic', 'sweetness', 'acidity', 'tanning', 'alcohol', 'body',
                  'flavourIntensity', 'flavourCharacteristic', 'finish', 'qualityLevel')
