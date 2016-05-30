import sys
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from intelliwineApp.bottleModel.bottle_vector_model import BottleVectorCharacteristics, BottleVectorFlavourAndAroma
from intelliwineApp.serializers import BottleVectorCharacSerializer, BottleVectorFlavourAndAroma
from intelliwineApp.similarity import cosine_similarity


@api_view(['GET', 'POST'])
def bottle_charac_vector_list(request):

    print >> sys.stdout, 'call bottle_vector_list\n'

    if request.method == 'GET':
        bottle_charac = BottleVectorCharacteristics.objects.all()
        serializer = BottleVectorCharacSerializer(bottle_charac, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BottleVectorCharacSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def compute_similarity(request):
    bottle_vectors_charac = BottleVectorCharacteristics.objects.all()
    bottle_vectors_flav_and_aroma = BottleVectorFlavourAndAroma.objects.all()

    serializer = BottleVectorCharacSerializer(data=request.data)
    serializer_vector_charac = BottleVectorCharacSerializer(bottle_vectors_charac, many=True)
    serializer_vector_flav_and_aroma = BottleVectorFlavourAndAroma(bottle_vectors_flav_and_aroma, many=True)

    score = 0

    if serializer.is_valid():

        content = JSONRenderer().render(serializer_vector_charac.data)
        json_data = json.loads(content)

        for vector in json_data:
            score = max(score, cosine_similarity(vector, serializer.data))

    return Response(score, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def bottle_vector_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """

    print >> sys.stdout, 'call bottle_vector_detail\n'

    try:
        bottle = BottleVector.objects.get(pk=pk)
    except BottleVector.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BottleVectorSerializer(bottle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BottleVectorSerializer(bottle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bottle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)