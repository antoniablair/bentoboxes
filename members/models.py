from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from sorl.thumbnail import ImageField
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import delete

# Create your models here.
class Member(AbstractUser):
    """
    Custom user class.
    """

    avatar = models.ImageField(upload_to='images/')
    occupation = models.TextField(max_length=300, blank=True)
    city = models.TextField(max_length=200, blank=True)
    state = models.TextField(max_length=200, blank=True)

