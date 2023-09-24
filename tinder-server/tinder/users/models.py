from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import Interests


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    interests = models.TextField(blank=True)
    description = models.TextField(blank=True)
    image = models.FileField(upload_to='users_images', null=True, default=None, blank=True)
    prefer_age_min = models.IntegerField(default=18)
    prefer_age_max = models.IntegerField(default=99)
    prefer_location = models.CharField(max_length=120, default='None')
    prefer_distance_min = models.IntegerField(default=1)
    prefer_distance_max = models.IntegerField(default=99)
class SharedProfile(models.Model):
    age = models.PositiveIntegerField()