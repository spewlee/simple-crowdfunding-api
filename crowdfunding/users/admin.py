from django.contrib import admin
from django.db import models


from .models import CustomUser

admin.site.register(CustomUser)