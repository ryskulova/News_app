from celery import shared_task
from django.core.mail import send_mail

@shared_task
def email_admin(message):
    """
    A test function for sending mail.
    """
    result = send_mail(
        message,
        'Here is the message.',
        'from@example.com',
        ['ryskulova_ai@auca.kg.com'],
        fail_silently=False,
    )
    return result