from django.db import models
from datetime import datetime



class showsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['rel_date']) > 0:
            if datetime.now() < datetime.strptime(postData['rel_date'], '%Y-%m-%d'):
                errors["rel_date"] = "Date should be in the past"
        else:
            errors["rel_date"] = "You should enter a date"
        if len(postData['desc']) < 10 and len(postData['desc']) > 0:
            errors["desc"] = "Description should be at least 10 characters"
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField(default="There is no description.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = showsManager()