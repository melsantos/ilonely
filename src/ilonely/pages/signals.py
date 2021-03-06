from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from pages.models import Profile
from pages.geo import getLocation

# Profile is created when after user is created
@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    # Do not create profile for superuser or staff
    if not instance.is_superuser and not instance.is_staff:
        if created:
            profile = Profile.objects.create(user=instance, age=18)
            profile.save()

# Location is set/updated whenever the sender logs in
@receiver(user_logged_in, sender=User)
def setLocation(sender, request, user, **kwargs):
    # Checks if user a superuser or staff
    if not user.is_superuser and not user.is_staff:
        userLocDict = getLocation()

        profile = Profile.objects.filter(user=user).first()
        profile.location = ("%s, %s") % (userLocDict["city"], userLocDict["region_code"])
        profile.latitude = userLocDict["latitude"]
        profile.longitude = userLocDict["longitude"]

        profile.save()
