# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .models import Driver,Addbooking
from django.contrib.auth.decorators import login_required
from .forms import UserForm,UserProfileInfoForm,DriverForm,AddbookForm
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.views.generic import TemplateView, ListView

def index(request):
    return render(request,'index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered =False
    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'login_home.html')

            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


def adddriver(request):
    form = DriverForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        db_obj = Driver(name=data['name'], mobile_number=data['mobile_number'], email=data['email'],
                          driver_id=data['driver_id'], address=data['address'], dl_no=data['dl_no'])
        db_obj.save()
        return HttpResponse("success")
    return render(request,'Driver_Add.html',{'form':DriverForm()})
def addbooking(request):
    form = AddbookForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        db_obj = Addbooking(user_name=data['user_name'],pickup_add=data['pickup_add'], drop_add=data['drop_add'],date=data['date'],time=data['time'])
        db_obj.save()
        return HttpResponse("success")
    return render(request,'add_booking.html',{'form':AddbookForm()})

def booking_data(request):
    x = Addbooking.objects.all()
    return render(request, 'my_bookings.html', {'objs': x})
