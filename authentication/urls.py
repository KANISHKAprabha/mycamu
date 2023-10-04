from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  
    path('signin/', views.signin, name='signin'),
    path('signup/signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/signin/home/', views.home, name='home'),
    
    
]
