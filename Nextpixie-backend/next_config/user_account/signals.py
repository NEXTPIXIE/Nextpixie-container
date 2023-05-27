import random
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from djoser.signals import user_registered, user_activated
from .helpers.mail import send_otp_mail
from django.utils import timezone
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from .models import UserOtp
from main.helpers.generators import generate_code


User = get_user_model()


@receiver(post_save, sender=User)
def send_welcome_mail(instance, created, **kwargs):
    print("here I am")
    if created:
        if instance.role == 'basic user':
            otp = generate_code()
            expiry_date = timezone.now() + timezone.timedelta(minutes=5)

            UserOtp.objects.create(user=instance, otp=otp, expiry_date=expiry_date)

            send_otp_mail(email=instance.email, first_name=instance.first_name.title(), otp=otp)
        else:
            return
    return