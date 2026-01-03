from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'

# Signal handler to create profile when user is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Use get_or_create to avoid duplicates
        Profile.objects.get_or_create(user=instance)

# Signal handler to save profile when user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Check if profile exists before saving
    if hasattr(instance, 'profile'):
        instance.profile.save()