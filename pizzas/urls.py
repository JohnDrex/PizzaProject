from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizs', views.pizs, name='pizs'),
    path('pizs/<int:pizza_name_id>/',views.pizza,name='pizza'),
    path('comments/<int:pizza_name_id>/',views.comments,name='comments'),

]