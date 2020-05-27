from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('register/', views.Register.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('edit/', views.EditProfile.as_view(), name='edit_profile')

]