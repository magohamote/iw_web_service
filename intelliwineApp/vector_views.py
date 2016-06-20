import json
import sys
import collections

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from intelliwineApp.bottle_serializers import BottleVectorCharacSerializer, BottleVectorFlavAromaSerializer, BottleSerializer
from intelliwineApp.bottle_vector_model import BottleVectorCharacteristics, BottleVectorFlavourAndAroma, Bottle
from intelliwineApp.user_serializers import UserAromaSerializer, UserCharacSerializer
from intelliwineApp.vector_reduction import create_user_charac_dict, create_user_aroma_mask, reduce_user_charac
from intelliwineApp.similarity import compute_cosine_similarity


@api_view(['POST'])
def post_bottle(request):
    print('call post_bottle\n', file=sys.stdout)

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

    print('call bottle_vector_list\n', file=sys.stdout)

    if request.method == 'GET':
        bottle_charac = BottleVectorCharacteristics.objects.all()
        bottle_flav_aroma = BottleVectorFlavourAndAroma.objects.all()

        serializer_charac = BottleVectorCharacSerializer(bottle_charac, many=True)
        serializer_flav_aroma = BottleVectorFlavAromaSerializer(bottle_flav_aroma, many=True)

        full_vector = serializer_charac.data, serializer_flav_aroma.data

        return Response(full_vector)

    elif request.method == 'POST':
        print('POST data = ', request.data, file=sys.stdout)

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

    if len(bottle_charac_serializer.data) != len(bottle_aroma_serializer.data):
        return Response("Data inconsistency in database", status=status.HTTP_406_NOT_ACCEPTABLE)

    for data in bottle_charac_serializer.data:
        charac_dict[data['bottle_foreign_id']] = data

    for data in bottle_aroma_serializer.data:
        aroma_dict[data['bottle_foreign_id']] = data

    sorted_bottle_charac = collections.OrderedDict(sorted(charac_dict.items()))
    sorted_bottle_aroma = collections.OrderedDict(sorted(aroma_dict.items()))

    if user_charac_serializer.is_valid() and user_aroma_serializer.is_valid():
        user_charac_content = JSONRenderer().render(user_charac_serializer.validated_data)
        user_aroma_content = JSONRenderer().render(user_aroma_serializer.validated_data)
        user_charac_json = json.loads(user_charac_content.decode('utf-8'))
        user_aroma_json = json.loads(user_aroma_content.decode('utf-8'))

        user_charac_dict = create_user_charac_dict(user_charac_json)
        user_aroma_dict = create_user_aroma_mask(user_aroma_json)

        unitary_user_aroma_vector = list()
        for _ in user_aroma_dict:
            unitary_user_aroma_vector.append(1)

        # print("user_charac_dict", file=sys.stdout)
        # print(user_charac_dict, file=sys.stdout)
        # print("\n", file=sys.stdout)
        #
        # print("user_aroma_dict", file=sys.stdout)
        # print(user_aroma_dict, file=sys.stdout)
        # print("\n", file=sys.stdout)
        #
        # print("sorted_bottle_charac", file=sys.stdout)
        # print(sorted_bottle_charac, file=sys.stdout)
        # print("\n", file=sys.stdout)
        #
        # print("sorted_bottle_aroma", file=sys.stdout)
        # print(sorted_bottle_aroma, file=sys.stdout)
        # print("\n", file=sys.stdout)
        #
        # print("unitary_user_aroma_vector", file=sys.stdout)
        # print(unitary_user_aroma_vector, file=sys.stdout)
        # print("\n", file=sys.stdout)

        answer = compute_cosine_similarity(user_charac_dict, user_aroma_dict, sorted_bottle_charac, sorted_bottle_aroma, unitary_user_aroma_vector)
        return Response(answer, status=status.HTTP_200_OK)

    return Response(0, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def bottle_vector_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """

    print('call bottle_vector_detail\n', file=sys.stdout)

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