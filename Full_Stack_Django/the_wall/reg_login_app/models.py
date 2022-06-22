from django.db import models
import re
import bcrypt
from .models import *

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "First Name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last Name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password hould be at least 8 characters"
        elif postData['password'] != postData['conf_pwd']:
                errors["password"] = "Paswords does not match" 
        #check the email format and if it is already exist
        user = Users.objects.filter(email=postData['email'])
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = "Invalid email"
        elif len(user)>0:
            errors['email'] = "There is already an account associated with that email address "
        return errors

    def login_validator(self, postData):
        error = {}
        if len(postData['password']) < 8:
            error["password"] = "Password hould be at least 8 characters"
        user = Users.objects.filter(email=postData['email']) 
        if len(user)==0:
            error['email'] = "Email address or password is inncorrect" 
        elif user[0].email != postData['email']: 
            error['email'] = "Email address or password is inncorrect"
        elif not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            error["password"] = "Email address or password is inncorrect"
        return error
    
class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    objects = UserManager()


    def __str__(self):
        return '{}'.format(self.first_name)
