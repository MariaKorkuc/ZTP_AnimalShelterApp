from rest_framework import  status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Users.api.serializers import RegisterSerializer

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
            token = Token.objects.get(user=user)
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)