from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.index),
    path("blogs", views.blogs),
    path("blogs/<int:id>", views.blogsId),
    path("add_data/name/<int:age>/email", views.student)
]

