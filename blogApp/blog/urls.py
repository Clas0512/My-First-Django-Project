from django.urls import path
from .views import *

urlpatterns = [
    path("", PostCreateView.as_view(), name="index"),
    path("list", PostListView.as_view(), name="listView"),
    path("register", UserCreateView.as_view(), name="createUser"),
]
