from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import datetime
from pprint import pprint
from .models import Post

#Создаем свои классы, которые наследуются от ListView и DetailView.
class PostList(ListView):
    model = Post
    ordering = '-time_of_creation'
    template_name = 'post_list.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        pprint(context)
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'
