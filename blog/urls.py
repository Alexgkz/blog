# blog/urls.py
from django.urls import path
 
from .views import (
            BlogListView, 
            BlogDetailView, 
            BlogCreateView,
            BlogUpdateView,# new  
            BlogDeleteView, # Импортируем представление
)
 
urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'), # Создаем новый маршрут
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), # Новый маршрут
    path('post/new/', BlogCreateView.as_view(), name='post_new'), # new
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # новое изменение
    path('', BlogListView.as_view(), name='home'),
]