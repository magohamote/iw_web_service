from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Bottle


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BottleSerializer(serializers.HyperlinkedModelSerializer):

    pk = serializers.IntegerField(read_only=True)
    sweetness = serializers.IntegerField(default=0)
    acidity = serializers.IntegerField(default=0)
    tannin = serializers.IntegerField(default=0)
    alcohol = serializers.IntegerField(default=0)
    body = serializers.IntegerField(default=0)
    flavour_intensity = serializers.IntegerField(default=0)

    class Meta:
        model = Bottle
        fields = ('sweetness', 'acidity', 'tannin', 'alcohol', 'body', 'flavour_intensity')

    def create(self, validated_data):
        return Bottle.object.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sweetness = validated_data.get('sweetness', instance.sweetness)
        instance.acidity = validated_data.get('acidity', instance.acidity)
        instance.tannin = validated_data.get('tannin', instance.tannin)
        instance.alcohol = validated_data.get('alcohol', instance.alcohol)
        instance.body = validated_data.get('body', instance.body)
        instance.flavour_intensity = validated_data('flavour_intensity', instance.flavour_intensity)
        instance.save()
        return instance
