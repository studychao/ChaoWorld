# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import RegisterForm,addForm
from .models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('../login')
    else:
        form = RegisterForm()

    return render(request,'register.html',context={'form':form})

def dashboard(request):
    return render(request,'dashboard.html')

def infochange(request):
    if request.method == 'POST':
        form = addForm(request.POST)

        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            username = request.POST['username']
            Userinfo = User.objects.get(username=username)
            Userinfo.nickname = nickname
            Userinfo.save()
            return render(request, 'dashboard.html')

    else:
        form = addForm()

    return render(request,'infochange.html',context={'form':form})