from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128, blank=True)  # Add password field

    def save(self, *args, **kwargs):
        # Save user's password to UserProfile
        self.password = self.user.password
        super().save(*args, **kwargs)
