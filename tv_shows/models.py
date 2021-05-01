from __future__ import unicode_literals
from django.db import models



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData["title"]) < 2:
            errors['title'] = "Tv show title should have at least 2 characters"

        if len(postData["network"]) < 3:
            errors['network'] = "Tv show network should have at least 3 characters"

        if len(postData["description"]) < 10:
            errors['description'] = "Tv show description should have at least 10 characters"
            
        return errors

class Show(models.Model):
    title = models.CharField( max_length=50)
    release_date = models.TextField(max_length=50)
    network = models.TextField(max_length=50)
    desc = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()


        
