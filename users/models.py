from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=100,
        unique=True,
        error_messages={"unique": "A user with that username already exists."},
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        error_messages={"unique": "This field must be unique."},
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
