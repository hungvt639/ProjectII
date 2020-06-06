from django.urls import path
from . import views
urlpatterns = [
    path('', views.Index_Room.as_view(), name='index_view'),
    path('<int:id>', views.Room.as_view(), name='room'),
    path('<int:id>/edit', views.Edit.as_view(), name='edit_room')
]
