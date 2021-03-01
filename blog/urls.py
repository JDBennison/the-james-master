from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('<blog_id>/', views.post_detail, name='post_detail'),
]
