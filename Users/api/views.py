from django.http import JsonResponse
from rest_framework import  status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from Users.api.serializers import RegisterSerializer, UserSerializer
from Users.models import User


@api_view(['POST',])
def registration_view(request):
    if request.method == "POST":
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Registration was successful. You can now log in."
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET',])
def logout_view(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET',])
@permission_classes([IsAuthenticated,])
def users_list_view(request):
    user = request.user

    if not (user.role == User.ADMIN or user.role == User.WORKER):
        return JsonResponse({'message': "You don't have enough permissions to do that"},
                            status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'GET':
        if user.role == User.ADMIN:
            users = User.objects.all()
        else:
            users = User.objects.filter(role=User.USER)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE','PUT'])
@permission_classes([IsAuthenticated,])
def user_view(request, pk):
    currentUser = request.user

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET' and user.role == User.USER \
            and (currentUser.role == User.ADMIN or currentUser.role == User.WORKER):
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT' and currentUser.role == User.ADMIN:
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
    elif request.method == 'DELETE' and currentUser.role == User.ADMIN:
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        return JsonResponse({'message': "You don't have enough permissions to do that"},
                            status=status.HTTP_401_UNAUTHORIZED)