from django.db import models
from django.contrib..auth.user import User 

class UserProfile(models.Model):
    user = models.OneToOneFeild(User, on_delete=models.CASCADE)
    name = models.CharFeild(max_length=255)
    email = models.EmailFeild(unique=True)
    phone_number = models.CharFeild(max_length=20, blank=True)

    def __str__(self):
        return self.name or self.user.username