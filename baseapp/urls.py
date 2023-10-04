from django.urls import path
from . import views



urlpatterns = [
  path('home/',views.Home_Page,name='page'),
  path('admin/',views.Admin_Page,name='admin'),
  path('student/',views.Student_Page,name='student'),
  path('teacher/',views.Teacher_Page,name='teacher'),
    
]
