from django.urls import path
from Users.api.views import registration_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = "Users"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
]