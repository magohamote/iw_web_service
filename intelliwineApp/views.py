import sys
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from intelliwineApp.serializers import UserSerializer, GroupSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    print('call UserViewSet', file=sys.stdout)
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    print('call GroupViewSet', file=sys.stdout)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
