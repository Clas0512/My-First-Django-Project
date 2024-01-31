from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


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

def kayit(request):
    # Eğer form gönderilmediyse, sadece formu göster
    if request.method == 'GET':
        form = StudentForm()
        return render(request, 'blog/kayitol.html', {'form': form})
    else:
        # Eğer form gönderildiyse, formu işle ve student-add'e yönlendir
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            new_entry = Student(name=name, age=age, email=email)
            new_entry.save()
            # Eğer işlem başarılı ise, student-add view'ına yönlendir
            return redirect('student-add')
        else:
            # Eğer form geçerli değilse, hata mesajları ile birlikte aynı sayfayı göster
            return render(request, 'blog/kayitol.html', {'form': form})

def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            new_entry = Student(name=name, age=age, email=email)
            new_entry.save()
            return HttpResponse("Veri basariiii")
    else:
        form = StudentForm()

    return render(request, 'blog/kayitol.html', {'form': form})

def student(request, name, age, email):
    new_entry = Student(name=name, age=age, email=email)
    new_entry.save()
    return HttpResponse("Veri basariiii")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
