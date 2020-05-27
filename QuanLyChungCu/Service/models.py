from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Service(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    status = models.BooleanField(default=True)


class Price_List(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cost = models.FloatField()
    note = models.TextField(max_length=1000)
    coefficient = models.FloatField()


class History(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField(max_length=1000)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.IntegerField() #tong tien
    cashier = models.ForeignKey(User, on_delete=models.CASCADE) #thu ngan






