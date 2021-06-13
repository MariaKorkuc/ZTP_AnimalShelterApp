from rest_framework import serializers
from AnimalShelterApp.models import Animal
from Users.models import User
from Users.api.serializers import UserSerializer
from rest_framework.fields import CurrentUserDefault

# class ChoiceField(serializers.ChoiceField):
#
#     def to_representation(self, obj):
#         if obj == '' and self.allow_blank:
#             return obj
#         return self._choices[obj]
#
#     def to_internal_value(self, data):
#         # To support inserts with the value
#         if data == '' and self.allow_blank:
#             return ''
#
#         for key, val in self._choices.items():
#             if val == data:
#                 return key
#         self.fail('invalid_choice', input=data)
from rest_framework.relations import PrimaryKeyRelatedField


class AnimalSerializer(serializers.ModelSerializer):
    # type = ChoiceField(choices=Animal.ANIMAL_TYPE)
    class Meta:
        model = Animal
        fields = ['id', 'name', 'age', 'weight', 'height', 'description', 'type', 'image']


class AnimalReservationSerializer(serializers.ModelSerializer):
    # reservedby = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = Animal
        fields = ['id', 'available']

    # def update(self, instance, validated_data):
    #     instance.available = False
    #     # instance.reservedby = CurrentUserDefault()
    #     instance.save()
    #     return instance