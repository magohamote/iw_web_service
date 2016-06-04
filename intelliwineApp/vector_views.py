import sys
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from intelliwineApp.bottleModel.bottle_vector_model import BottleVectorCharacteristics, BottleVectorFlavourAndAroma
from intelliwineApp.serializers import BottleVectorCharacSerializer, BottleVectorFlavAromaSerializer
from intelliwineApp.similarity import cosine_similarity


@api_view(['GET', 'POST'])
def bottle_charac_vector_list(request):

    print >> sys.stdout, 'call bottle_vector_list\n'

    if request.method == 'GET':
        print >> sys.stdout, 'GET'

        bottle_charac = BottleVectorCharacteristics.objects.all()
        bottle_flav_aroma = BottleVectorFlavourAndAroma.objects.all()

        serializer_charac = BottleVectorCharacSerializer(bottle_charac, many=True)
        serializer_flav_aroma = BottleVectorFlavAromaSerializer(bottle_flav_aroma, many=True)

        full_vector = serializer_charac.data, serializer_flav_aroma.data

        return Response(full_vector)

    elif request.method == 'POST':
        print >> sys.stdout, 'POST data = ', request.data

        serializer_charac = BottleVectorCharacSerializer(data=request.data[0])
        serializer_flav_aroma = BottleVectorFlavAromaSerializer(data=request.data[1])

        if serializer_charac.is_valid() and serializer_flav_aroma.is_valid():

            serializer_charac.save()
            serializer_flav_aroma.save()
            return Response([serializer_charac.data, serializer_flav_aroma.data], status=status.HTTP_201_CREATED)
        return Response([serializer_charac.errors, serializer_flav_aroma.errors], status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def compute_similarity(request):
    bottle_vectors_charac = BottleVectorCharacteristics.objects.all()
    bottle_vectors_flav_and_aroma = BottleVectorFlavourAndAroma.objects.all()

    serializer_vector_charac = BottleVectorCharacSerializer(bottle_vectors_charac, many=True)
    serializer_vector_flav_and_aroma = BottleVectorFlavAromaSerializer(bottle_vectors_flav_and_aroma, many=True)

    print >> sys.stdout, serializer_vector_flav_and_aroma.data.sort()

    serializer_user = BottleVectorCharacSerializer(data=request.data)

    serializer_vector_charac = BottleVectorCharacSerializer(bottle_vectors_charac, many=True)

    score = 0

    if serializer_user.is_valid():

        content = JSONRenderer().render(serializer_vector_charac.data)
        json_data = json.loads(content)

        for vector in json_data:
            score = max(score, cosine_similarity(vector, serializer_user.data))

        return Response(score, status=status.HTTP_200_OK)

    return Response(score, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def bottle_vector_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """

    print >> sys.stdout, 'call bottle_vector_detail\n'

    try:
        bottle = BottleVectorCharacteristics.objects.get(pk=pk)
    except BottleVectorCharacteristics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BottleVectorCharacSerializer(bottle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BottleVectorCharacSerializer(bottle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bottle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)