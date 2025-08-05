from django.db import models
from django.contrib.auth.user import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name or self.user.username