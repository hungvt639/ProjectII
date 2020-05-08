from django.urls import path
from .views import Index_Notify, Send_Notify
urlpatterns = [
    path('', Index_Notify.as_view(), name='index_notify'),
    path('send', Send_Notify.as_view(), name='send_notify')
    # path('notification/', include('Notification.urls'))
]