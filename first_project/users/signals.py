from django.db.models.signals import post_save # fire a signal when an object is saved
from django.contrib.auth.models import User # the sender sending the signal
from django.dispatch import receiver # receive signal to run function
from .models import Profile # create user profile automatically when a user is created

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    When a user is saved, send signal to receiver which is this function.
    Then, it will receive argument values from post_save:
    instance : instance of User object
    created : check if the User is created
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()        
