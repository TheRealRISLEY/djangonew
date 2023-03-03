from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Student


def index_page(request):
    data = Student.objects.all()
    context = {'data': data}
    return render(request, "index.html", context)


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def edit_Page(request):
    return render(request, "edit.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        country = request.POST.get('country')

        query = Student(name=name, email=email, age=age, gender=gender, phone=phone, country=country)
        query.save()
        return redirect("/")

        return render(request, "/")


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        gender = request.POST.get('gender')

        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.phone = phone
        update_info.country = country
        update_info.gender = gender

        update_info.save()
        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
