from django.urls import path
from .views import Index_Notify, Send_Notify, Create_Notify, Edit_Notify, Delete_notify, View_notify
urlpatterns = [
    path('', Index_Notify.as_view(), name='index_notify'),
    path('new', Create_Notify.as_view(), name='new_notify'),
    path('send/<int:id>', Send_Notify.as_view(), name='send_notify'),
    path('edit/<int:id>', Edit_Notify.as_view(), name='edit_notify'),
    path('delete/<int:id>', Delete_notify.as_view(), name='delete_notify'),
    path('<int:id>', View_notify.as_view(), name='view_notify')
    # path('notification/', include('Notification.urls'))
]