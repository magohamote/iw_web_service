from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import BottleDNA


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BottleSerializer(serializers.HyperlinkedModelSerializer):
    clarity = serializers.CharField(max_length=16)
    colorSimple = serializers.CharField(max_length=10)
    color = serializers.CharField(max_length=16)
    observations1 = serializers.CharField(max_length=256)
    condition = serializers.CharField(max_length=16)
    intensity = serializers.CharField(max_length=16)
    aromaCharacteristic = serializers.CharField(max_length=2048)
    development = serializers.CharField(max_length=32)
    sweetness = serializers.CharField(max_length=16)
    acidity = serializers.CharField(max_length=16)
    tanning = serializers.CharField(max_length=16)
    alcohol = serializers.CharField(max_length=16)
    body = serializers.CharField(max_length=16)
    flavourIntensity = serializers.CharField(max_length=16)
    flavourCharacteristic = serializers.CharField(max_length=2048)
    observations2 = serializers.CharField(max_length=256)
    finish = serializers.CharField(max_length=16)
    qualityLevel = serializers.CharField(max_length=16)
    structure = serializers.CharField(max_length=256)
    balance = serializers.CharField(max_length=256)
    concentration = serializers.CharField(max_length=256)
    complexity = serializers.CharField(max_length=256)
    length = serializers.CharField(max_length=256)
    typicity = serializers.CharField(max_length=256)
    levelOfReadiness = serializers.CharField(max_length=64)
    appellation = serializers.CharField(max_length=256)
    region = serializers.CharField(max_length=256)
    country = serializers.CharField(max_length=256)
    variety = serializers.CharField(max_length=256)
    vintage = serializers.CharField(max_length=256)
    productionMethod = serializers.CharField(max_length=256)
    climaticInfluences = serializers.CharField(max_length=256)
    nameOfTheWine = serializers.CharField(max_length=256)
    nameOfTheWinery = serializers.CharField(max_length=256)
    typeOfSweetness = serializers.CharField(max_length=16)
    typeOfCarbonDioxide = serializers.CharField(max_length=16)
    typeOfViscosity = serializers.CharField(max_length=16)
    typeOfAlcohol = serializers.CharField(max_length=16)
    typeOfAcid = serializers.CharField(max_length=16)
    typeOfFruit = serializers.CharField(max_length=16)
    typeOfTannin = serializers.CharField(max_length=16)
    ripeness = serializers.CharField(max_length=16)
    freshness = serializers.CharField(max_length=16)
    harmony = serializers.CharField(max_length=16)

    class Meta:
        model = BottleDNA
        fields = ('clarity', 'colorSimple', 'color', 'observations1', 'condition', 'intensity', 'aromaCharacteristic', 'development', 'sweetness', 'acidity', 'tanning', 'alcohol', 'body', 'flavourIntensity', 'flavourCharacteristic', 'observations2', 'finish', 'qualityLevel', 'structure', 'balance', 'concentration', 'complexity', 'length', 'typicity', 'levelOfReadiness', 'appellation', 'region', 'country', 'variety', 'vintage', 'productionMethod', 'climaticInfluences', 'nameOfTheWine', 'nameOfTheWinery', 'typeOfSweetness', 'typeOfCarbonDioxide', 'typeOfViscosity', 'typeOfAlcohol', 'typeOfAcid', 'typeOfFruit', 'typeOfTannin', 'ripeness', 'freshness', 'harmony')

    def create(self, validated_data):
        return BottleDNA.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.clarity = validated_data.get('clarity', instance.clarity)
        instance.colorSimple = validated_data.get('colorSimple', instance.colorSimple)
        instance.color = validated_data.get('color', instance.color)
        instance.observations1 = validated_data.get('observations1', instance.observations1)
        instance.condition = validated_data.get('condition', instance.condition)
        instance.intensity = validated_data.get('intensity', instance.intensity)
        instance.aromaCharacteristic = validated_data.get('aromaCharacteristic', instance.aromaCharacteristic)
        instance.development = validated_data.get('development', instance.development)
        instance.sweetness = validated_data.get('sweetness', instance.sweetness)
        instance.acidity = validated_data.get('acidity', instance.acidity)
        instance.tanning = validated_data.get('tanning', instance.tanning)
        instance.alcohol = validated_data.get('alcohol', instance.alcohol)
        instance.body = validated_data.get('body', instance.body)
        instance.flavourIntensity = validated_data.get('flavourIntensity', instance.flavourIntensity)
        instance.flavourCharacteristic = validated_data.get('flavourCharacteristic', instance.flavourCharacteristic)
        instance.observations2 = validated_data.get('observations2', instance.observations2)
        instance.finish = validated_data.get('finish', instance.finish)
        instance.qualityLevel = validated_data.get('qualityLevel', instance.qualityLevel)
        instance.structure = validated_data.get('structure', instance.structure)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.concentration = validated_data.get('concentration', instance.concentration)
        instance.complexity = validated_data.get('complexity', instance.complexity)
        instance.length = validated_data.get('length', instance.length)
        instance.typicity = validated_data.get('typicity', instance.typicity)
        instance.levelOfReadiness = validated_data.get('levelOfReadiness', instance.levelOfReadiness)
        instance.appellation = validated_data.get('appellation', instance.appellation)
        instance.region = validated_data.get('region', instance.region)
        instance.country = validated_data.get('country', instance.country)
        instance.variety = validated_data.get('variety', instance.variety)
        instance.vintage = validated_data.get('vintage', instance.vintage)
        instance.productionMethod = validated_data.get('productionMethod', instance.productionMethod)
        instance.climaticInfluences = validated_data.get('climaticInfluences', instance.climaticInfluences)
        instance.nameOfTheWine = validated_data.get('nameOfTheWine', instance.nameOfTheWine)
        instance.nameOfTheWinery = validated_data.get('nameOfTheWinery', instance.nameOfTheWinery)
        instance.typeOfSweetness = validated_data.get('typeOfSweetness', instance.typeOfSweetness)
        instance.typeOfCarbonDioxide = validated_data.get('typeOfCarbonDioxide', instance.typeOfCarbonDioxide)
        instance.typeOfViscosity = validated_data.get('typeOfViscosity', instance.typeOfViscosity)
        instance.typeOfAlcohol = validated_data.get('typeOfAlcohol', instance.typeOfAlcohol)
        instance.typeOfAcid = validated_data.get('typeOfAcid', instance.typeOfAcid)
        instance.typeOfFruit = validated_data.get('typeOfFruit', instance.typeOfFruit)
        instance.typeOfTannin = validated_data.get('typeOfTannin', instance.typeOfTannin)
        instance.ripeness = validated_data.get('ripeness', instance.ripeness)
        instance.freshness = validated_data.get('freshness', instance.freshness)
        instance.harmony = validated_data.get('harmony', instance.harmony)

        instance.save()

        return instance
