from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    Model to store user detail with extending the default User model

    `User`
        User Instance

    `location`
        Location of user
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=20)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

