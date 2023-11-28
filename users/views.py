from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserSerializer


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    """
    API view for create a user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
