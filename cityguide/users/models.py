from django.db import models
from django.contrib.auth.models import AbstractUser


class Interest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)


class Profile(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField()
    location = models.CharField(max_length=64)
    discretionary_income = models.IntegerField()
    miles_willing_to_travel = models.IntegerField()
    # mobility
    group_person_count = models.IntegerField()
    interests = models.ManyToManyField(Interest)


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
