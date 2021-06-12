from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from AnimalShelterApp.api.serializers import AnimalSerializer
from AnimalShelterApp.models import Animal


@api_view(['GET',])
def animal_list(request):
    if request.method == 'GET':
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)


@api_view(['POST',])
@permission_classes([IsAuthenticated,])
def animal_add(request):

    user = request.user
    print(user.WORKER)

    if not (user.role == user.ADMIN or user.role == user.WORKER):
        return JsonResponse({'message': "You don't have enough permissions to do that"}, status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'POST':
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated,])
def animal_detail(request, pk):
    try:
        animal = Animal.objects.get(pk=pk)
    except Animal.DoesNotExist:
        return JsonResponse({'message': 'The animal does not exist'}, status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if request.method == 'GET':
        serializer = AnimalSerializer(animal)
        return Response(serializer.data)

    elif (user.role == user.ADMIN or user.role == user.WORKER):
        if request.method == 'PUT':
            serializer = AnimalSerializer(animal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
        elif request.method == 'DELETE':
            animal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return JsonResponse({'message': "You don't have enough permissions to do that"}, status=status.HTTP_401_UNAUTHORIZED)

