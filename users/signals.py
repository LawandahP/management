from django.db.models.signals import post_save
from .models import Profile, CustomUser


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
        )
        print('profile created')


post_save.connect(create_profile, sender=CustomUser)


# def update_profile(sender, instance, created, **kwargs):
#     if not created:
#         instance.profile.save()
#         print('profile updated')
#
#
# post_save.connect(update_profile, sender=CustomUser)
