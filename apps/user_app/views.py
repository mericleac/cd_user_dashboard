from django.shortcuts import render, redirect
from .models import *

def user_dashboard(request):
    return render(request, 'user_app/user_dashboard.html', { 'users': User.objects.all(), 'user':User.objects.get(id=request.session['current_user']) })

def show(request, user_id):
    return render(request, 'user_app/show.html', { 'show_user': User.objects.get(id=int(user_id)), 'user': User.objects.get(id=request.session['current_user']), 'messages': User.objects.get(id=user_id).dashboard_messages.all() })

def edit(request, user_id):
    user = User.objects.get(id=request.session['current_user'])
    return render(request, 'user_app/user_edit.html', { 'user': user, 'errors': request.session['errors'] })

def process_edit(request):
    user = User.objects.get(id=request.session['current_user'])
    if request.POST['changed'] == 'information':
        errors = User.objects.edit_information(request.POST)
        if len(errors):
            request.session['errors'] = errors
            return redirect('/user/edit')
        user.email = request.POST['email']
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
    elif request.POST['changed'] == 'password':
        errors = User.objects.edit_password(request.POST)
        if len(errors):
            request.session['errors'] = errors
            return redirect('/user/edit')
        import bcrypt
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user.hashed_password = hashed_pw
        user.save()
    elif request.POST['changed'] == 'description':
        user.description = request.POST['description']
        user.save()
    return redirect('/user/dashboard')
        
def create_message(request, user_id):
    message = Message(message=request.POST['content'], user_posted=User.objects.get(id=request.session['current_user']), user_dashboard=User.objects.get(id=user_id))
    message.save()
    return redirect( '/user/' + user_id + '/show')

def create_comment(request, user_id, message_id):
    comment = Comment(comment=request.POST['content'], message= Message.objects.get(id=message_id), user= User.objects.get(id=request.session['current_user']))
    comment.save()
    return redirect( '/user/' + user_id + '/show')

def delete_message(request, user_id, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect('/user/' + user_id + '/show')

def delete_comment(request, user_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('/user/' + user_id + '/show')
