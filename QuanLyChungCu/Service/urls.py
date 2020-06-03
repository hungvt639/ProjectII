from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index_Service.as_view(), name='index_service')
    # path('notification/', include('Notification.urls'))
]