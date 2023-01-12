from django.contrib import admin
from django.urls import path
from . import views

app_name="personal"

urlpatterns = [
    path("",views.home,name="home"),
    path('exp/',views.experience,name="exp"),
    path('project/',views.project,name="project"),
    path('project/pythn',views.pythn,name="pythn"),
    
    
  
]