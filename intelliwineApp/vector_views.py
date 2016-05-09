import sys, json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from intelliwineApp.models import BottleVector
from intelliwineApp.serializers import BottleVectorSerializer
from intelliwineApp.similarity import cosine_similarity, get_json_value


@api_view(['GET', 'POST'])
def bottle_vector_list(request):

    print >> sys.stdout, 'call bottle_vector_list\n'

    if request.method == 'GET':
        bottle = BottleVector.objects.all()
        serializer = BottleVectorSerializer(bottle, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BottleVectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def compute_similarity(request):
    bottle_vectors = BottleVector.objects.all()

    serializer = BottleVectorSerializer(data=request.data)
    serializer_vector = BottleVectorSerializer(bottle_vectors, many=True)

    if serializer.is_valid():

        content = JSONRenderer().render(serializer_vector.data)
        json_data = json.loads(content)

        score = 0
        for vector in json_data:
            x = get_json_value(vector)
            y = get_json_value(serializer.data)
            score = max(score, cosine_similarity(x, y))

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