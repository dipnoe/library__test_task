from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


@shared_task
def send_welcome_message(recipient_email):
    send_mail(
        subject='Добро пожаловать!',
        message='Вы успешно зарегистрированы на нашем сервисе.',
        from_email=EMAIL_HOST_USER,
        recipient_list=[recipient_email]
    )
