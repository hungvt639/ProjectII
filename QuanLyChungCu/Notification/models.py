from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notify(models.Model):
    manage_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manage_id")
    heading = models.CharField(max_length=1000)
    content = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.heading


class Notify_User(models.Model):
    notify_id = models.ForeignKey(Notify, on_delete=models.CASCADE, related_name="notify_id")
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="id_user")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} to {1}".format(self.notify_id, self.id_user)