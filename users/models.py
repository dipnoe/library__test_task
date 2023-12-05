from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    first_name = models.CharField(max_length=255, verbose_name='имя')
    last_name = models.CharField(max_length=255, verbose_name='фамилия')
    email = models.EmailField(verbose_name='электронная почта', unique=True)
    date_joined = models.DateTimeField(auto_now_add=True,
                                       verbose_name='дата регистрации',
                                       help_text='автоматически заполняется при создании пользователя')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.first_name.title()} {self.last_name.title()}'
