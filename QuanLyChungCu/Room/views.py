from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Rooms
from django.contrib.auth.models import User


class Index_Room(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            rooms = Rooms.objects.all().order_by('id')
            return render(request, 'room_manage.html', {'rooms': rooms})
        else:
            try:
                room = Rooms.objects.get(room_master = request.user)
            except:
                room = None
            return render(request, 'room.html', {'room': room})


        # for i in range(1, 17):
        #     for j in range (1, 12):
        #         r = Rooms()
        #         r.building = ''
        #         x=''
        #         if i < 10:
        #            x += '0' + str(i)
        #         elif i==13:
        #             x+='12A'
        #         else:
        #             x+= str(i)
        #         x+='-'
        #         if j < 10:
        #             x += '0' + str(j)
        #         else:
        #             x+= str(j)
        #         r.address = x
        #         r.area = 80
        #         r.number_bedrooms=2
        #         r.save()


class Room(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            room = Rooms.objects.filter(pk=id).first
            return render(request, 'room_manage_id.html', {'room': room})
        else:
            room = Rooms.objects.filter(pk=id, room_master=request.user).first
            return render(request, 'room_id.html', {'room': room})


class Edit(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            room = Rooms.objects.filter(pk=id).first
            users = User.objects.all()
            return render(request, 'edit_room.html', {'room': room, 'users': users})
        else:
            return redirect('room', id=id)

    def post(self, request, id):
        if request.user.is_staff:
            try:
                room = Rooms.objects.get(pk=id)
                room.area = request.POST['area']
                room.number_bedrooms = request.POST['number_bedrooms']
                room_master = User.objects.get(pk=request.POST['room_master'])
                room.room_master = room_master
                room.save()
                return redirect('room', id=id)
            except Exception as e:
                raise e
        else:
            return redirect('room', id=id)