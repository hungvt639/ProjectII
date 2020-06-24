from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.



class Index(LoginRequiredMixin,View):


    def get(self, request):
        if request.user.is_staff:
            return render(request, 'index_manage.html')
        else:
            return render(request, 'index.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        errors = []
        try:
            user = User()
            user.username = request.POST['username']
            user.email = request.POST['email']
            if User.objects.filter(Q(username=user.username) | Q(email=user.email)).exists():
                errors.append('User đã tồn tại')
                return render(request, 'register.html', {'errors': errors})
            else:
                password = request.POST['password']
                repassword = request.POST['repassword']
                if password == repassword:
                    user.set_password(password)
                    user.first_name = request.POST['firstname']
                    user.last_name = request.POST['lastname']
                    user.save()
                    return redirect("login")
                else:
                    errors.append("Nhập lại mật khẩu không hợp lệ")
                    return render(request, 'register.html', {'errors':errors})
        except Exception as e:
            raise e
        

class Profile(LoginRequiredMixin, View):

    def get(self, request):
        return render(request, "view_profile.html")


class EditProfile(LoginRequiredMixin, View):

    def get(self,request):
        return render(request, "edit_profile.html")

    def post(self, request):
        try:
            user = User.objects.get(pk=request.user.id)
            user.first_name = request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.email = request.POST['email']
            user.save()
            return redirect('profile')
        except Exception as e:
            raise e


class ChangePassword(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'changepassword.html')

    def post(self, request):
        errors = []
        try:
            oldpassword = request.POST['oldpassword']
            password = request.POST['password']
            repassword=request.POST['repassword']
            if repassword == password:
                user = User.objects.get(pk=request.user.id)
                if user.check_password(oldpassword):
                    user.set_password(password)
                    user.save()
                    return redirect('index')
                else:
                    errors.append('Nhập sai mật khẩu cũ')
                    return render(request, 'changepassword.html', {'errors': errors})

            else:
                errors.append('Mật khẩu mới không khớp')
                return render(request, 'changepassword.html', {'errors': errors})

        except:
            return redirect('sos')

class sos(View):
    def get(self, request):
        return render(request, 'sos.html')