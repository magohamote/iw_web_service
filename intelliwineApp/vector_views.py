import json
import sys
import collections

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from intelliwineApp.bottle_serializers import BottleVectorCharacSerializer, BottleVectorFlavAromaSerializer, BottleSerializer
from intelliwineApp.bottle_vector_model import BottleVectorCharacteristics, BottleVectorFlavourAndAroma, Bottle
from intelliwineApp.user_serializers import UserSerializer, UserAromaSerializer, UserCharacSerializer
from intelliwineApp.similarity import cosine_similarity


@api_view(['POST'])
def post_bottle(request):
    print >> sys.stdout, 'call post_bottle\n'

    bottle_serializer = BottleSerializer(data=request.data[0])
    if bottle_serializer.is_valid():
        bottle_serializer.save()

        last_bottle = Bottle.objects.latest('id')
        last_bottle_serialized = BottleSerializer(last_bottle)

        charac_serializer = BottleVectorCharacSerializer(data=request.data[1])
        flav_aroma_serializer = BottleVectorFlavAromaSerializer(data=request.data[2])

        if charac_serializer.is_valid() and flav_aroma_serializer.is_valid():
            charac_serializer.validated_data['bottle_foreign_key'] = last_bottle
            charac_serializer.validated_data['bottle_foreign_id'] = last_bottle_serialized.data['id']

            flav_aroma_serializer.validated_data['bottle_foreign_key'] = last_bottle
            flav_aroma_serializer.validated_data['bottle_foreign_id'] = last_bottle_serialized.data['id']

            charac_serializer.save()
            flav_aroma_serializer.save()
            return Response(bottle_serializer.data, status=status.HTTP_201_CREATED)

    return Response(bottle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
    bottle_charac = BottleVectorCharacteristics.objects.all()
    bottle_aroma = BottleVectorFlavourAndAroma.objects.all()

    bottle_charac_serializer = BottleVectorCharacSerializer(bottle_charac, many=True)
    bottle_aroma_serializer = BottleVectorFlavAromaSerializer(bottle_aroma, many=True)

    user_charac_serializer = UserCharacSerializer(data=request.data['charac'], many=False)
    user_aroma_serializer = UserAromaSerializer(data=request.data['aroma'], many=False)

    charac_dict = dict()
    aroma_dict = dict()

    for data in bottle_charac_serializer.data:
        charac_dict[data['bottle_foreign_id']] = data

    for data in bottle_aroma_serializer.data:
        aroma_dict[data['bottle_foreign_id']] = data

    sorted_charac = collections.OrderedDict(sorted(charac_dict.items()))
    sorted_aroma = collections.OrderedDict(sorted(aroma_dict.items()))




    # serializer_user = BottleVectorCharacSerializer(data=request.data)
    #
    # score = 0
    #
    # if serializer_user.is_valid():
    #
    #     vector_charac_content = JSONRenderer().render(serializer_vector_charac.data)
    #     vector_charac_json_data = json.loads(vector_charac_content)
    #
    #     for vector in vector_charac_json_data:
    #         score = max(score, cosine_similarity(vector, serializer_user.data))
    #
    #     return Response(score, status=status.HTTP_200_OK)

    return Response(0, status=status.HTTP_400_BAD_REQUEST)


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