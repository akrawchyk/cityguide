from django.db import models
from django.contrib.auth.models import AbstractUser


class Interest(models.Model):
    name = models.CharField(max_length=64)


class Profile(models.Model):
    age = models.IntegerField
    location = models.CharField(max_length=64)
    discretionary_income = models.IntegerField()
    miles_willing_to_travel = models.IntegerField()
    # mobility
    group_person_count = models.IntegerField()
    interests = models.ManyToManyField(Interest)


class User(AbstractUser):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
