
from django.db import IntegrityError
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.template import loader
from django.http import HttpResponse





def home(request):
    return render(request,'authentication/index.html')



def signup(request):
    if request.method == 'POST':
        user_role = request.POST.get('choose')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            myuser = User.objects.create_user(username=name, password=password,email=email)
            myuser.user_role = user_role
            myuser.name = name
            myuser.save()

            messages.success(request, "Your account is created successfully")
            return render(request, 'authentication/signin.html')  # Render the signin.html template
        except IntegrityError:
            messages.error(request, "This email is already in use.")
            return render(request, 'authentication/index.html')  # Render the home.html template

    # Handle the GET request if needed
    return render(request, 'authentication/signup.html')  # Render the signup.html template





def signin(request):
    if request.method == 'POST':
        
        
        name=request.POST.get('name')
        password = request.POST.get('password')
        user=authenticate(password=password,username=name)
        if user is not None:
            login(request,user)
            return redirect('home')

        else:
            messages.error(request,'Bad credentials')
            return redirect('signin')
    return render (request,'siginup')


   

def signout(request):
        
           logout(request)
           messages.error(request,'Logged out sucessfully')
           return redirect('home')

# def authentication(request):
#     template = loader.get_template('authentication/index.html')
#     return HttpResponse(template.render())

        





# Create your views here.
