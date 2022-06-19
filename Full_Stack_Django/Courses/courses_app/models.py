from django.db import models

class coursesManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Description should be at least 15 characters"
        return errors

class Courses(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(default='There is no description')
    comment=models.TextField()    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = coursesManager()