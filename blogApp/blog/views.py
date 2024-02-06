from typing import Any
from django.contrib.auth import authenticate, login
from django.db.models.query import QuerySet
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Post


from django.views.generic.base import TemplateView


class ChatPageView(TemplateView):
    template_name = 'blog/chat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_data'] = 'Bu veri home2.html içinde kullanılabilir.'
        return context

class HomePageView(TemplateView):
    template_name = "blog/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('/')


class UserLogoutView(LogoutView):
    template_name = 'blog/logout.html'
    redirect_authenticated_user = False
    success_url = reverse_lazy('/')


class PostCreateView(LoginRequiredMixin, CreateView):
    # model = User
    # fields = ['username', 'password', 'email', 'is_active', 'is_staff']
    model = Post
    success_url = '/post'
    fields = ['title', 'content', 'owner']
    template_name = 'blog/post.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        else:
            return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_authenticated'] = self.request.user.is_authenticated
        return context


class UserDetailView(DetailView):
	model = Post
	template_name = 'blog/details-user.html'
	context_object_name = 'user_details'

class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'blog/user-register.html'
    success_url = '/'


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(form.cleaned_data['password'])
        obj.save()
        return super(UserCreateView, self).form_valid(form)
