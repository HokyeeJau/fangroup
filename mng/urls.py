from django.urls import path

from . import views

urlpatterns = [
    path('', views.mng, name='mng'),
]
