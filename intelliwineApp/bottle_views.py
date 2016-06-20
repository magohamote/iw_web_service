import sys
from rest_framework import viewsets
from intelliwineApp.bottle_serializers import BottleDNASerializer
from .bottle_dna_model import BottleDNA
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class BottleViewSet(viewsets.ModelViewSet):
    print('call BottleViewSet', file=sys.stdout)
    queryset = BottleDNA.objects.all().order_by('nameOfTheWine')
    serializer_class = BottleDNASerializer


@api_view(['GET', 'POST'])
def bottle_dna_list(request):
    """
    List all bottles, or create a new bottle DNA.
    """

    print('call bottle_dna_list\n', file=sys.stdout)

    if request.method == 'GET':
        bottle = BottleDNA.objects.all()
        serializer = BottleDNASerializer(bottle, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BottleDNASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def bottle_dna_detail(request, pk):
    """
    Retrieve, update or delete a bottle DNA instance.
    """

    print('call bottle_dna_detail\n', file=sys.stdout)

    try:
        bottle = BottleDNA.objects.get(pk=pk)
    except BottleDNA.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BottleDNASerializer(bottle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BottleDNASerializer(bottle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bottle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)