from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index),
    path("blogs", views.blogs),
    path("blogs/<int:id>", views.blogsId),
    #
    path("<int:question_id>/", views.detail, name="detail"),
    path("kayitol/", views.kayit, name="kayit-ol"),
    path("kayitol/", views.student, name="student-add"),
]
