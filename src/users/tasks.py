from celery import shared_task
from django.core.mail import send_mail

from src.config.settings import EMAIL_HOST_USER


@shared_task
def send_welcome_message(recipient_email, recipient_name):
    subject = 'Добро пожаловать.'
    message = (f'Здравствуйте, {recipient_name}!'
               f'Вы успешно зарегистрированы на нашем сервисе.')
    send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[recipient_email]
    )
