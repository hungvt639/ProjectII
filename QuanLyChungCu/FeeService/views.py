from django.shortcuts import render
from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from Service.models import Service, Service_Using
from Notification.models import Notify, Notify_User
from Room.models import Rooms, Member_Room
import datetime
# Create your views here.
