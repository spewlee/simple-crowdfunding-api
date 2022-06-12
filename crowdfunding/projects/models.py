from django.contrib.auth import get_user_model
from django.db import models

# Project Model
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    goal_amount = models.IntegerField(default=0)
    amount_raised = models.IntegerField(default=0)
    image = models.URLField(null=True, blank=True, default="https://media.istockphoto.com/photos/various-sports-equipment-balls-on-wooden-background-picture-id1145660545?b=1&k=20&m=1145660545&s=170667a&w=0&h=-oZeH_yvbCkH4S4t8XrPpqb3UykS8dntaa693L_6r4A=")
    date_created = models.DateField(auto_now=True)
    due_date = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date_created']


# Pledge Model
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.TextField()
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='supporter'
    )



# Comment Model
class Comment(models.Model):
    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name='comment'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comment'
    )
    date = models.DateField(auto_now=True)
    body = models.TextField(blank=False)

    class Meta:
        ordering = ['date']