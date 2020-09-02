from __future__ import unicode_literals
from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 5:
            errors['title'] = "Title name should be 5 or more characters"
        if len(postData['network']) < 5:
            errors['network'] = "Network should be 5 or more characters"
        if len(postData['description']) < 10:
            errors['description'] = "Description should be 10 or more characters"
        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()