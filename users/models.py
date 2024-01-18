from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    groups = None
    user_permissions = None
    def __str__(self) -> str:
        return f'{self.id}: {self.first_name} {self.last_name}'