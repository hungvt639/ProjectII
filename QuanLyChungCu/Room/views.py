from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Rooms, Member_Room
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
            room = Rooms.objects.filter(pk=id).first()
            if room:
                member = Member_Room.objects.filter(room=room.id)
            else: member = []
            return render(request, 'room_manage_id.html', {'room': room, 'member': member})
        else:
            member = Member_Room.objects.filter(room=id)
            r = member.filter(user=request.user).first
            return render(request, 'room_id.html', {'room': r, 'member': member})

    def post(self, request, id):
        if request.user.is_staff:
            try:
                member = User.objects.filter(pk=request.POST['member']).first()
                Member_Room.objects.filter(user=member).delete()
                return redirect('room', id=id)
            except:
                return redirect('sos')
        else:
            return redirect('sos')


class Edit(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            room = Rooms.objects.filter(pk=id).first()
            member = Member_Room.objects.filter(room=room.id)
            users = User.objects.filter(is_staff=False).exclude(id__in=member.values_list("user", flat=True))
            return render(request, 'edit_room.html', {'room': room, 'users': users, 'member': member})
        else:
            return redirect('room', id=id)

    def post(self, request, id):
        if request.user.is_staff:
            try:
                room = Rooms.objects.get(pk=id)
                user = User.objects.get(pk=request.POST['member'])
                user_room = Member_Room.objects.filter(room=room, user=user).first()
                if not user_room:
                    user_room = Member_Room()
                    user_room.room = room
                    user_room.user = user
                    user_room.save()
                return redirect('edit_room', id=id)
            except Exception as e:
                raise e
        else:
            return redirect('room', id=id)