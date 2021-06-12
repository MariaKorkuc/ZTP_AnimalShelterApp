from django.urls import path
from Users.api.views import registration_view, logout_view, users_list_view, user_view
from rest_framework.authtoken.views import obtain_auth_token

app_name = "Users"

urlpatterns = [
    path('register', registration_view, name="register"),
    path('login', obtain_auth_token, name="login"),
    path('logout', logout_view, name="logout"),
    path('', users_list_view, name="logout"),
    path('<int:pk>', user_view, name="logout"),
]