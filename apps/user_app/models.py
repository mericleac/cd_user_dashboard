from django.db import models
from apps.login_reg_app.models import *

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_posted = models.ForeignKey(User, related_name="messages")
    user_dashboard = models.ForeignKey(User, related_name="dashboard_messages")

class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    message = models.ForeignKey(Message, related_name="comments")
    user = models.ForeignKey(User, related_name="comments")
