from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.


def index(request):
    # return HttpResponse("Home Page")
    return render(request, "blog/index.html")


def blogs(request):
    # return HttpResponse("Blogs")
    return render(request, "blog/blogs.html")


def blogsId(request, id):
    # return HttpResponse("Blog Number: " + str(id))
    return render(request, "blog/blog-id.html", {
        "id": id
    })

def student(request, name, age, email):
    new_entry = Student(name, age, email)
    new_entry.save()
    return HttpResponse("Veri basariiii")