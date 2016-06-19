# ModelSerializer classes don't do anything particularly magical,
# they are simply a shortcut for creating serializer classes:
#   - An automatically determined set of fields.
#   - Simple default implementations for the create() and update() methods.

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')