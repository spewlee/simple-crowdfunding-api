from django.contrib.auth.models import AbstractUser
from django.db import models


# User Model
class CustomUser(AbstractUser):
    profile_pic = models.URLField(null=True, blank=True, default="https://images.nightcafe.studio//assets/profile.png?tr=w-1600,c-at_max")

    def __str__(self):
        return self.username



