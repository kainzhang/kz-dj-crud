from django.urls import path
from vip import views

app_name = 'vip'

urlpatterns = [
    path('', views.vip_list, name='vip_list'),
    path('new', views.vip_insert, name='vip_new'),
    path('edit/<int:pk>', views.vip_update, name='vip_edit'),
    path('delete/<int:pk>', views.vip_delete, name='vip_remove'),
    path('select', views.vip_select, name='vip_search'),
]