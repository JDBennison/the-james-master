from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.PostList, name='blog'),
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
]
