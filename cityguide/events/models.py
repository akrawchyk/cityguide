from django.db import models


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    when = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=64)
    age_min = models.IntegerField(blank=True)
    primary_contact = models.ForeignKey

    def __str__(self):
        return f'{self.name}'
