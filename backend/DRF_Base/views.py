from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.exceptions import BadRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from DRF_Base.models import User


def index(request):
    return render(request, 'index.html', {})


def register_page(request):
    logout(request)
    return render(request, 'register.html', {})


def login_page(request):
    return render(request, 'login.html', {})


def confirm_email(request, code):
    if User.objects.filter(email_validation_code=code).exists():
        user = User.objects.get(email_validation_code=code)
        user.is_validated = True
        user.save()
        return render(request, 'confirm_email.html')
    else:
        return HttpResponse('<h1> 404 not found </h1>')


def log_out(request):
    logout(request)
    print(request.user)
    return redirect('/register')
