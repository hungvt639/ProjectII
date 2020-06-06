from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Service
# Create your views here.

class Index_Service(LoginRequiredMixin ,View):
    def get(self, request):
        if request.user.is_staff:
            # staff
            services = Service.objects.all().order_by('-id')
            return render(request, 'index_service_manage.html', {'services':services})
        else:
            pass

class New_Service(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, 'new_service_manage.html')
        else:
            pass

    def post(self, request):
        if request.user.is_staff:
            try:
                service = Service()
                service.admin = request.user
                service.name = request.POST['name']
                service.cost = request.POST['cost']
                service.coefficient = request.POST['coefficient']
                service.note = request.POST['note']
                service.save()
                return redirect('index_service')
            except Exception as e:
                raise e
        else:
            pass

class Edit(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            service = Service.objects.filter(pk=id).first
            return render(request, 'edit_service_manage.html')