from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Notify, Notify_User

# Create your views here.
from django.views import View


class Index_Notify(View):
    def get(self, request):
        if request.user.is_staff == False:
            notify = Notify_User.objects.filter(id_user=request.user.id).order_by("created")
            return render(request, 'index_notify.html', {"notify": notify})
        else:
            return redirect('send_notify')


class Send_Notify(View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, "send_notify.html")
        else:
            return redirect('index_notify')