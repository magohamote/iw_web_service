from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from intelliwineApp.serializers import UserSerializer, GroupSerializer, BottleSerializer
from .models import Bottle


# Create your views here.
def index(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class BottleViewSet(viewsets.ModelViewSet):
    queryset = Bottle.objects.all().order_by('color')
    serializer_class = BottleSerializer

