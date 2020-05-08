from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notify(models.Model):
    manage_id = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notify_User(models.Model):
    notify_id = models.ForeignKey(Notify, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)