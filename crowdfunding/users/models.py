from django.contrib.auth.models import AbstractUser
from django.db import models


# User Model
class CustomUser(AbstractUser):
    profile_pic = models.URLField(null=True)

    def __str__(self):
        return self.username



