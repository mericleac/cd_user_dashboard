from django.shortcuts import render, redirect
from .models import *

def index(request):
    request.session['errors'] = {}
    return render(request, 'user_app/index.html')

def login(request):
    if 'errors' not in request.session:
        request.session['errors'] = {}
    return render(request, 'user_app/login.html', { 'errors': request.session['errors'] })

def process_login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        request.session['errors'] = errors
        return redirect('/login')
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['current_user'] = user.id
        request.session['errors'] = {}
        if user.user_level < 9:
            return redirect('/user/dashboard')
        else:
            return redirect('/admin/dashboard')

def register(request):
    if 'errors' not in request.session:
        request.session['errors'] = {}
    return render(request, 'user_app/register.html', { 'errors': request.session['errors'] })

def process_register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        request.session['errors'] = errors
        return redirect('/register')
    else:
        import bcrypt
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], hashed_password=hashed_pw)
        all_users = User.objects.all()
        if len(all_users) == 0:
            user.user_level = 9
        else:
            user.user_level = 1
        user.save()
        request.session['current_user'] = user.id
        request.session['errors'] = {}
        if user.user_level < 9:
            return redirect('/user/dashboard')
        else:
            return redirect('/admin/dashboard')

