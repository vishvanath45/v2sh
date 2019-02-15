# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django import forms
from .forms import RegisterForm,LoginForm
from django.http import HttpResponse
from v2sh.environment import db, experience, superuser, credentials,session
import hashlib
from django.utils.crypto import get_random_string

'''
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage,send_mail
from .sent import sent_mail
# ,LoginForm

# from .models import user
# Create your views here.

# def authenticate(request):
#     return render(request, 'accounts/authenticate.html')
#

User = get_user_model()
# @login_required()

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            sender  = "support@v2sh.in"
            user = form.save(commit=False)
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('accounts/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
                'sender': sender
            })
            to_email = form.cleaned_data.get('email')
            sent_mail(message , to_email)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})
#
# def login(request):
#     form  = LoginForm()
#     if request.method == 'POST':
#         email = request.POST['email']
#         passwd = request.POST['password']
#         try:
#             User = user.objects.get(email = email ,pwd = passwd)
#             return render(request, 'contents/home.html', {'User': User})
#         except:
#             return render(request, 'accounts/login.html', {'form': form})
#
#     return render(request , 'accounts/login.html' , {'form' : form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
'''
def hash(string):
    m = hashlib.sha256()
    m.update(string.encode())
    return m.digest()  

def signup(request):
   # if request.session['email']:
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = hash(form.cleaned_data.get('password1'))
            full_name = form.cleaned_data.get('name')
            is_authenticate = False
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
            secret_key = get_random_string(20, chars) 
            key = hashlib.sha256((secret_key + email).encode('utf-8')).hexdigest()    
            credentials.insert({'Name' : full_name , 'Email' : email , 'Password' : password1 , 'is_authenticate' : is_authenticate , 'key' : key})
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})
        
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = hash(form.cleaned_data.get('password'))
            if credentials.find_one({'Email' : email , 'Password' : password , 'is_authenticate' : True}) != None:
                return redirect('home')
            else:
            #request.session['email'] = email
                return redirect('login')
    else:
        form = LoginForm()
    
    return render(request, 'accounts/login.html', {'form': form})
    
def logout(request):
    return redirect('home')

def activation(request , key):
    if credentials.find_one({'key' : key}) != None:
        if credentials.find_one({'key' : key , 'is_authenticate' : False}) != None:
            credentials.update_one({'key' : key , 'is_authenticate' : False} , {"$set" : {'is_authenticate' : True}})                                                                                      
            return redirect('login')
        else:
            return redirect('home')
    else:
        return redirect('signup')

