from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from intelliwineApp.serializers import UserSerializer, GroupSerializer, BottleSerializer
from .models import BottleDNA
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
    queryset = BottleDNA.objects.all().order_by('nameOfTheWine')
    serializer_class = BottleSerializer


@api_view(['GET', 'POST'])
def bottle_list(request, format=None):
    """
    List all bottles, or create a new bottle.
    """
    if request.method == 'GET':
        bottle = BottleDNA.objects.all()
        serializer = BottleSerializer(bottle, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BottleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def bottle_detail(request, pk, format=None):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        bottle = BottleDNA.objects.get(pk=pk)
    except BottleDNA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BottleSerializer(bottle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BottleSerializer(bottle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bottle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
