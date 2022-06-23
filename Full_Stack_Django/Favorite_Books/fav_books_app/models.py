import re
from django.db import models
from reg_login_app.models import Users

class bookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['desc']) < 5:
            errors["desc"] = "Description should be at least 5 characters"
        return errors
    
class Books(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(Users, related_name='books_uploaded', on_delete = models.CASCADE)
    liked_books = models.ManyToManyField(Users, related_name='liked')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = bookManager()
