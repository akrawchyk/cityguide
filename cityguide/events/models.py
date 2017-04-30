from django.db import models


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    starts_at = models.DateTimeField(blank=True, null=True)
    ends_at = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=64)
    age_min = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)
    primary_contact = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    attendees = models.ManyToManyField('users.User',
                                       related_name='event_attendees')
    interests = models.ManyToManyField('interests.Interest',
                                       related_name='event_interests')

    def __str__(self):
        return f'{self.name}'
