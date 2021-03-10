from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_booking, name='view_booking'),
]
