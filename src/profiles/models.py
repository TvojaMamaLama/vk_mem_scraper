from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    """Custom user model"""
    vk_token = models.CharField('Token from vk app', max_length=300)
