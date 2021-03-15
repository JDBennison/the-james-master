from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking, name='booking'),
    path('calculate-cost/', views.calculate_cost, name="calculate_cost"),
    path('checkout/', views.checkout, name="checkout"),
    path('save_booking/', views.save_booking, name="save_booking"),
]
