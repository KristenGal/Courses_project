from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Course
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=Course)
def course_created_signal(sender, instance, created, **kwargs):
    if created:
        from_email = settings.DEFAULT_FROM_EMAIL
        message = f"A new course titled '{instance.title}' has been created by {instance.teacher.full_name}. Thank you for being a part of our community!"
        to_email = instance.teacher.email
        send_mail(
            "New Course Created",
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )
