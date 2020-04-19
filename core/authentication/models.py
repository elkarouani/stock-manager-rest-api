from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_provider = models.BooleanField(verbose_name="Is Provider ?", default=False)
