from django.contrib.auth.password_validation import validate_password
from django.forms import ChoiceField
from rest_framework import serializers
from Users.models import User

class RegisterSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        # fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password2')
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        # extra_kwargs = {
        #     'password2': {'write_only': True}
        # }

    def validate(self, attr):
       validate_password(attr['password'])
       return attr

    def save(self):
        user = User.objects.create(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        password = self.validated_data['password']
        # password2 = self.validated_data['password2']
        #
        # if password != password2:
        #     raise serializers.ValidationError({'password': "Passwords don't match"})
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    role = ChoiceField(choices=User.ROLE)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'email']


