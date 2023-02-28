from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def index_page(request):
    return render(request, "index.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def edit_Page(request):
    return render(request, "edit.html")
