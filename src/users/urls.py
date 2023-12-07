from django.urls import path

from src.users.apps import UsersConfig
from src.users.views import UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create')
]
