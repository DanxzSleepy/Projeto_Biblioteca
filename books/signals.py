from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Member

@receiver(post_save, sender=User)
def create_user_member(sender, instance, created, **kwargs):
    """
    Automatically create a Member profile when a User is created
    """
    if created:
        # Check if a Member profile already exists for this user
        if not hasattr(instance, 'member'):
            Member.objects.create(
                user=instance,
                phone_number="",
                role='member'  # Default role is member
            )

@receiver(post_save, sender=User)
def save_user_member(sender, instance, **kwargs):
    """
    Save the Member profile when the User is saved
    """
    if hasattr(instance, 'member'):
        instance.member.save()