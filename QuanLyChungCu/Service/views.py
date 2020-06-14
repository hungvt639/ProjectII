from django.db.models.functions import Coalesce
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Service, Service_Using
from ..Notification.models import Notify, Notify_User
from Room.models import Rooms, Member_Room
import datetime
# Create your views here.


class Index_Service(LoginRequiredMixin, View):
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
            try:
                service = Service.objects.get(pk=id)
                if service.status == False:
                    return redirect("sos")
                member_room = Member_Room.objects.filter(user=request.user)
                rooms = Rooms.objects.filter(id__in=member_room.values_list("room", flat=True))
            except Exception as e:
                return redirect('sos')
            return render(request, 'rigister_service.html', {'service': service, 'rooms': rooms})

    def post(self, request, id):
        if request.user.is_staff:
            return redirect('sos')
        else:
            try:
                service = Service.objects.get(pk=id)
                room = request.POST['room']
                if service.status == False:
                    return redirect("sos")
                member_room = Member_Room.objects.filter(room=room)
                users = User.objects.filter(id__in=member_room.values_list("user", flat=True))
                if request.user in users:
                    service_using = Service_Using()
                    service_using.service = service
                    service_using.user = request.user
                    service_using.room = member_room[0].room
                    service_using.note = request.POST['note']
                    s = Service_Using.objects.filter(service=service, room=room).first()
                    if not s:
                        service_using.save()
                else:
                    return redirect('sos')
            except Exception as e:
                raise e
                # return redirect('sos')
            return redirect('list_register_service')


class List_Register_Service(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            service_using = Service_Using.objects.filter(status_register=False).order_by('room', '-id')
            return render(request, "list_register_service_manage.html", {'serviceusing': service_using})
        else:
            member_room = Member_Room.objects.filter(user=request.user)
            try:
                room = request.GET['room']
            except:
                room = None
            if room:
                member_room.filter(room=room)
            service_using = Service_Using.objects.filter(status_register=False, room__in=member_room.values_list('room', flat=True)).order_by('room', '-id')
            return render(request, 'list_register_service.html', {'service_using': service_using})


class Destroy_Service(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            try:
                service_using = Service_Using.objects.get(pk=id)
                if service_using.status_register == False:
                    service_using.delete()
                return redirect('list_register_service')
            except:
                return redirect('sos')
        else:
            try:
                service_using = Service_Using.objects.get(pk=id)
                if service_using.user == request.user and service_using.status_register == False:
                    service_using.delete()
                return redirect('list_register_service')
            except:
                return redirect('sos')


class Activate_Service(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            try:
                service_using = Service_Using.objects.get(pk=id)
                service_using.status_register = True
                service_using.time_start = datetime.datetime.now()
                if service_using.save():
                    notify = Notify()
                    notify.heading = 'Đăng ký sử dụng dịch vụ thành công'
                    notify.content = """
                    Dịch vụ {0} của bạn đã được duyệt.
                    Tên dịch vụ {0}
                    Phòng {1}
                    Người đăng ký {2}
                    Thời gian {3}
                    """.format(service_using.service, service_using.room, service_using.user.get_full_name(), service_using.time_start)
                    notify.save()
                    room = Rooms.objects.get(pk=service_using.room.id)
                    member = Member_Room.objects.filter(room=room)
                    users = User.objects.filter(id__in=member.values_list('user', flat=True))
                    for u in users:
                        notify_user = Notify_User()
                        notify_user.id_user = u
                        notify_user.notify_id = notify
                        notify_user.save()

            except:
                return redirect('sos')
            return redirect('list_register_service')
        else:
            return redirect('sos')