from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Service(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    status = models.BooleanField(default=True)
    cost = models.FloatField()  # gia
    coefficient = models.FloatField(default=1)  # he so
    note = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class History(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=1000)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.IntegerField() #tong tien
    cashier = models.ForeignKey(User, on_delete=models.CASCADE) #thu ngan
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)







