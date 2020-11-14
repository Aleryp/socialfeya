from django.urls import path
from . import views


urlpattarns = [
    path('add', views.AddFollowerView),
    path('', views.ListFollowerView)
]