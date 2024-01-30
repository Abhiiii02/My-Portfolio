from django.urls import path
from . import views
from django.contrib import admin


admin.site.site_header = "Login to Developer Abhishek's Portfolio"
admin.site.site_title = "Welcome to Abhishek's Portfolio"
admin.site.index_title = "Welcome to Abhishek's Portfolio"

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('projects/',views.projects, name='projects'),
    path('contact',views.contact, name='contact'),


]
