from django.urls import path
from staff import views

app_name = 'staff'

urlpatterns = [
    path('', views.staff_list, name='staff_list'),
    path('new', views.staff_insert, name='staff_new'),
    path('edit/<int:pk>', views.staff_update, name='staff_edit'),
    path('delete/<int:pk>', views.staff_delete, name='staff_remove'),
    path('select', views.staff_select, name='staff_search'),
]