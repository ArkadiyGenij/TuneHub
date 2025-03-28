from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='адрес электронной почты')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='номер телефона')

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
