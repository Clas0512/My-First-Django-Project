import hashlib

from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Post


class PostCreateView(CreateView):
    # model = User
    # fields = ['username', 'password', 'email', 'is_active', 'is_staff']
    model = Post
    success_url = '/'
    fields = ['title', 'content', 'owner']
    template_name = 'blog/register.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'post_list'


class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'blog/user-register.html'
    success_url = '/'

    def form_valid(self, form):
        obj = form.save()
        obj.set_password(form.cleaned_data['password'])
        super().form_valid(form)
