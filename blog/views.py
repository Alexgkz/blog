# blog/views.py
from django.views.generic import ListView, DetailView # новое
from django.views.generic.edit import CreateView, UpdateView, DeleteView # новое изменение
from django.urls import reverse_lazy 
from .models import Post
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView): # новое
    model = Post
    template_name = 'post_detail.html'

    
class BlogCreateView(CreateView): # новое изменение
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    
class BlogUpdateView(UpdateView): # Новый класс
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    
class BlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')