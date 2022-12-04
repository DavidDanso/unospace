from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from .models import *
from django.core.mail import send_mail
from django.conf import settings

################### User Signals ################
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            name = user.first_name,
            email = user.email
        )

        subject = 'Unospace Email'
        message = f'Welcome to Unospace🔴🔐 {user.first_name}'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
        )

def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.email = profile.email
        user.username = profile.username
        user.save()

def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)

