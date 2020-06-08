from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Service
from Room.models import Rooms, Member_Room
# Create your views here.


class Index_Service(LoginRequiredMixin ,View):
    def get(self, request):
        if request.user.is_staff:
            # staff
            services = Service.objects.all().order_by('-id')
            return render(request, 'index_service_manage.html', {'services':services})
        else:
            services = Service.objects.filter(status=True).order_by('-id')
            return render(request, 'index_service.html', {'services': services})


class Show_Service(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            service = Service.objects.filter(pk=id).first
            return render(request, 'show_service_manage.html', {'service': service})
        else:
            service = Service.objects.filter(pk=id).first
            return render(request, 'show_service.html', {'service': service})


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
            service = Service.objects.filter(pk=id).first()
            return render(request, 'edit_service_manage.html', {'service': service})
        else:
            return redirect('sos')

    def post(self, request, id):
        if request.user.is_staff:
            try:
                service = Service.objects.get(pk=id)
                service.admin = request.user
                service.name = request.POST['name']
                try:
                    service.status = request.POST['status'] == "on"
                except:
                    service.status = False
                service.cost = request.POST['cost']
                service.coefficient = request.POST['coefficient']
                service.note = request.POST['note']
                service.save()
                return redirect('show_service', id=id)
            except Exception as e:
                raise e
        else:
            return redirect('sos')


class Delete_service(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            try:
                Service.objects.get(pk=id).delete()
            except: pass
            return redirect('index_service')
        else:
            return redirect('sos')


class Register_Service(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            return redirect('sos')
        else:
            service = Service.objects.filter(pk=id)
            member_room = Member_Room.objects.filter(user=request.user)
            return render(request, 'rigister_service.html', {'service': service, 'member_room': member_room})