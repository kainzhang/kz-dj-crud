from django.urls import path
from sale import views

app_name = 'sale'

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('new/', views.sale_insert, name='sale_new'),
    path('delete/<int:pk>', views.sale_delete, name='sale_remove'),
    path('select/', views.sale_select_date, name='sale_search_date'),
]