from django.db import models
from reg_login_app.models import Users


class Messages(models.Model):
    messages = models.TextField()
    user = models.ForeignKey(Users, related_name="messages", on_delete = models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

class comments(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Messages, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(Users, related_name="comment", on_delete = models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)