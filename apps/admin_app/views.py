from django.shortcuts import render, redirect
from .models import *

def admin_dashboard(request):
    user = User.objects.get(id=request.session['current_user'])
    if user.user_level < 9:
        return redirect('/user/dashboard')
    else:
        return render(request, 'user_app/admin_dashboard.html', { 'users': User.objects.all(), 'user': user })
    
def add(request):
    return render(request, 'user_app/add.html', { 'user': User.objects.get(id=request.session['current_user'])})

def process_add(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors):
        request.session['errors'] = errors
        return redirect('/admin/add')
    else:
        import bcrypt
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = User(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], hashed_password=hashed_pw)
        user.user_level = 1
        user.save()
        request.session['errors'] = {}
        return redirect('/admin/dashboard')

def admin_edit(request, user_id):
    return render(request, 'user_app/admin_edit.html', { 'errors': request.session['errors'], 'edit_user': User.objects.get(id=user_id), 'user': User.objects.get(id=request.session['current_user']) })

def process_edit(request, user_id):
    edit_user = User.objects.get(id=user_id)
    if request.POST['changed'] == 'information':
        if request.POST['email'] != edit_user.email:
            errors = User.objects.email_unique(request.POST)
            return redirect('/admin/' + user_id + '/edit')
        errors = User.objects.edit_information(request.POST)
        if len(errors):
            request.session['errors'] = errors
            return redirect('/admin/' + user_id + '/edit')
        edit_user.email = request.POST['email']
        edit_user.first_name = request.POST['first_name']
        edit_user.last_name = request.POST['last_name']
        edit_user.user_level = int(request.POST['user_level'])
        edit_user.save()
    elif request.POST['changed'] == 'password':
        errors = User.objects.edit_password(request.POST)
        if len(errors):
            request.session['errors'] = errors
            return redirect('/admin' + user_id + '/edit')
        import bcrypt
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        edit_user.hashed_password = hashed_pw
        edit_user.save()
    return redirect('/admin/dashboard')

def delete(request, user_id):
    user = User.objects.get(id=user_id)
    user.delete()
    return redirect('/admin/dashboard')
