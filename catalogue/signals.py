from django.db.models.signals import post_save, post_delete
from django.dispatch import Signal
from .models import Profile
from django.contrib.auth.models import User

def createProfile(sender, instance: User,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email=user.email
        )


def deleteUser(sender, instance: Profile,**kwargs):
    user = instance.user
    user.delete()

def updateUser(sender, instance: Profile, created, **kwargs):
    profile = instance
    user: User = profile.user
    
    if not created:
        user.username = profile.username
        user.email = profile.email
        user.save()

post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)
