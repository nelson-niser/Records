from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('check/', views.check, name='check'),
    path('history/', views.history, name='history'),
    path('checkall/', views.checkall, name='checkall'),
]