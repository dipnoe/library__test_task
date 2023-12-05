from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers import UserSerializer
from users.tasks import send_welcome_message
from rest_framework.response import Response


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    """
    API view for create a user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                send_welcome_message.delay(user.email, user.__str__())
                return Response(status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'result': f"Возникла ошибка {e}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
