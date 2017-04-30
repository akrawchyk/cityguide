from django.db import models


class Interest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
