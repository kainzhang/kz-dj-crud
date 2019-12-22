from django.urls import path
from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.goods_list, name='goods_list'),
    path('new', views.goods_insert, name='goods_new'),
    path('edit/<int:pk>', views.goods_update, name='goods_edit'),
    path('delete/<int:pk>', views.goods_delete, name='goods_remove'),
    path('select', views.goods_select, name='goods_search'),
    path('increase/<int:pk>', views.goods_increase, name='goods_add'),
]