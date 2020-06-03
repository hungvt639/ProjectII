from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# Create your views here.

class Index_Service(LoginRequiredMixin ,View):
    def get(self, request):
        if request.user.is_staff:
            # staff
            pass
        else:
            pass