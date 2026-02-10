from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),  # Strona główna z postami
    path('create/', views.post_create, name='post_create'),
    path('edit/<int:post_id>/', views.post_edit, name='post_edit'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('like/<int:post_id>/', views.post_like, name='post_like'),
]