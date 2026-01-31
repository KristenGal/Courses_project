from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=CustomUser)
def course_created_signal(sender, instance, created, **kwargs):
    if created:
        from_email = settings.DEFAULT_FROM_EMAIL
        message = f"Welcome to our project, {instance.full_name}! Thank you for registering."
        to_email = instance.email
        send_mail(
            "Welcome to Courses library",
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )
