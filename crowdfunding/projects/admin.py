from django.contrib import admin
from django.db import models


from .models import Comment, Pledge, Project

admin.site.register(Comment)
admin.site.register(Pledge)
admin.site.register(Project)
