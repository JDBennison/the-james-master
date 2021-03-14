from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('calculate-cost/', views.calculate_cost, name="calculate_cost")
]
