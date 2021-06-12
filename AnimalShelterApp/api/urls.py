from django.urls import path
from AnimalShelterApp.api.views import animal_list, animal_detail, animal_add

app_name = "AnimalShelterApp"

urlpatterns = [
    path('animals', animal_list, name="animals"),
    path('animals/add', animal_add, name="animals_add"),
    path('animals/<int:pk>', animal_detail, name="animals_det"),
]