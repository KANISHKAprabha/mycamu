from django.shortcuts import render
from urllib import request
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.template import RequestContext, loader
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def Home_Page(request):
    template = loader.get_template('baseapp/page.html')
    return HttpResponse(template.render())

@csrf_protect
def role_choice(request):
    form=RoleForm()
    if request.method=='POST':
        form=RoleForm(request.POST)
        if form.is_valid():
            options=form.cleaned_data['options']
            if options=='Admin':
                print("redirect to admin")
                return redirect('admin')
            elif options=='Student':
                return redirect('student')
            elif options=='Teacher':
                return redirect('teacher')
        
    return render(request,'page.html')

def Admin_Page(request):
    return render(request,'admin.html')
def Student_Page(request):
    return render(request,'student.html')
def Teacher_Page(request):
    return render(request,'teacher.html')