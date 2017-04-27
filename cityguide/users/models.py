from django.db import models
from django.contrib.auth.models import AbstractUser


class Interest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserProfile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateField(blank=True)
    location = models.CharField(max_length=64)
    discretionary_income = models.IntegerField()
    miles_willing_to_travel = models.IntegerField()
    # mobility
    group_person_count = models.IntegerField()
    interests = models.ManyToManyField(Interest)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.user.username}\'s profile'
