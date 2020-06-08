from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Rooms(models.Model):
    building = models.CharField(max_length=5)
    address = models.CharField(max_length=10)
    area = models.FloatField()
    number_bedrooms = models.IntegerField()
    # room_master = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.building+ ' ' + self.address)


class Member_Room(models.Model):
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} ( {1} )".format(self.room, self.user.get_full_name())